"""Run documented copy commands only against disposable paths, never installed skills."""
from pathlib import Path
import hashlib
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = 'challenge-and-refine-ideas'


class InstallAndBuild(unittest.TestCase):
    def test_absolute_external_archive_and_sidecar(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'bundle.zip'
            sidecar = Path(temporary) / 'SHA256SUMS'
            run = subprocess.run([sys.executable, str(ROOT/'tools/build_release.py'),
                                  '--output', str(output), '--checksum-output', str(sidecar)],
                                 capture_output=True, text=True, timeout=30)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(sidecar.read_text().split(), [hashlib.sha256(output.read_bytes()).hexdigest().upper(), output.name])
            version = (ROOT/'VERSION').read_text().strip()
            self.assertEqual(output.read_bytes(), (ROOT/f'dist/{NAME}-v{version}.zip').read_bytes())

    def snippet(self, readme, language):
        text = (ROOT/readme).read_text(encoding='utf-8')
        block = re.search(rf'```{language}\n(.*?)\n```', text, re.S).group(1)
        return '\n'.join(line for line in block.splitlines() if not line.startswith('git clone '))

    def exercise_copy(self, language, executable):
        for readme in ('README.md', 'README.zh-CN.md'):
            for existing in ('absent', 'directory', 'file'):
                with self.subTest(readme=readme, existing=existing), tempfile.TemporaryDirectory() as temporary:
                    base = Path(temporary)
                    source = base/NAME/'skill'/NAME
                    source.mkdir(parents=True)
                    (source/'SKILL.md').write_text('new entry')
                    target = base/'isolated skills'/NAME
                    target.parent.mkdir()
                    if existing == 'directory':
                        target.mkdir()
                        (target/'SKILL.md').write_text('keep local edit')
                    elif existing == 'file':
                        target.write_text('keep existing file')
                    snippet = self.snippet(readme, language)
                    if language == 'powershell':
                        lines = snippet.splitlines()
                        lines[0] = "$destination = '" + str(target).replace("'", "''") + "'"
                        command = [executable, '-NoProfile', '-NonInteractive', '-Command', '\n'.join(lines)]
                    else:
                        snippet = snippet.replace('destination=~/.codex/skills/'+NAME,
                                                  'destination='+shlex.quote(target.as_posix()))
                        command = [executable, '-c', snippet]
                    run = subprocess.run(command, cwd=base, capture_output=True, text=True, timeout=30)
                    if existing == 'absent':
                        self.assertEqual(run.returncode, 0, run.stderr)
                        self.assertEqual((target/'SKILL.md').read_text(), 'new entry')
                    else:
                        self.assertNotEqual(run.returncode, 0, run.stdout)
                        self.assertEqual((target/'SKILL.md').read_text() if target.is_dir() else target.read_text(),
                                         'keep local edit' if existing == 'directory' else 'keep existing file')
                    self.assertFalse((target/NAME).exists(), 'must never nest a second package')

    @unittest.skipUnless(shutil.which('pwsh') or shutil.which('powershell'), 'PowerShell unavailable')
    def test_documented_powershell_install(self):
        self.exercise_copy('powershell', shutil.which('pwsh') or shutil.which('powershell'))

    @unittest.skipUnless(os.name != 'nt' and shutil.which('bash'), 'POSIX shell tested on Linux CI')
    def test_documented_posix_install(self):
        self.exercise_copy('bash', shutil.which('bash'))

    def test_install_links_and_broken_symlink_guard_are_present(self):
        for readme in ('README.md', 'README.zh-CN.md'):
            self.assertIn('[ -L "$destination" ]', self.snippet(readme, 'bash'))
            self.assertIn('Get-Item -LiteralPath $destination -Force', self.snippet(readme, 'powershell'))
            self.assertIn('AI_INSTALL.md#updating-an-existing-installation', (ROOT/readme).read_text(encoding='utf-8'))
        html = (ROOT/'docs/index.html').read_text(encoding='utf-8')
        owner = 'fanfanfanfanfan626'
        owners = re.findall(r'https://github\.com/((?:fan)+626)/', html)
        self.assertTrue(owners)
        self.assertEqual(set(owners), {owner})


if __name__ == '__main__':
    unittest.main()
