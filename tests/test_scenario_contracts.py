"""Static protocol contracts, not live-model or host E2 evidence."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];PACKAGE=ROOT/'skill/challenge-and-refine-ideas'
SKILL=(PACKAGE/'SKILL.md').read_text(encoding='utf-8')
FIRST=(PACKAGE/'references/first-use-scenarios.md').read_text(encoding='utf-8')
EXAMPLES=(ROOT/'EXAMPLES.md').read_text(encoding='utf-8')
CHARTER=(PACKAGE/'assets/idea-charter.template.md').read_text(encoding='utf-8')
GUIDE=(PACKAGE/'references/idea-charter.md').read_text(encoding='utf-8')
STATUSES=('open','requires evidence','resolved by change','resolved by evidence','accepted trade-off','rejected by human')
class ScenarioContracts(unittest.TestCase):
    def test_five_copy_paste_intents(self):
        for intent in ('explore','refine','compare','challenge','decide'):
            self.assertRegex(FIRST,rf'(?s)## `{intent}`\n\n```text\n.+?\n```')
    def test_decision_boundaries(self):
        for text,marker in [(SKILL,'Do not force an `explore` session to produce a recommendation'),(FIRST,'Do not recommend, decide, or prescribe an experiment'),(FIRST,'challenge the current latest version'),(SKILL,'description of the **current candidate**'),(FIRST,'Separate verified evidence from adviser opinion'),(SKILL,'Separate supplied facts, external evidence'),(SKILL,'Do not execute or hand off a consequential high-risk action'),(FIRST,'prohibit consequential execution until required review is complete')]:self.assertIn(marker,text)
    def test_objection_states(self):
        self.assertIn(', '.join(f'`{s}`' for s in STATUSES[:-1])+f', or `{STATUSES[-1]}`',SKILL)
        self.assertIn('`'+' | '.join(STATUSES)+'`',CHARTER)
        for status in STATUSES:self.assertIn(f'`{status}`',FIRST)
        for text in (SKILL,FIRST,EXAMPLES,CHARTER):self.assertNotIn('evidence-needed',text)
    def test_three_axes(self):
        axes={'maturity':('raw','framed','expanded','challenged','decision-ready'),'evidence_state':('discussion-useful','test-needed','review-needed','sufficient-for-scope'),'human_disposition':('undecided','adopted','parked','rejected')}
        labels={'maturity':'Maturity','evidence_state':'Evidence state','human_disposition':'Human disposition'}
        for axis,values in axes.items():
            canonical=(' → ' if axis=='maturity' else ' | ').join(values)
            for text in (SKILL,GUIDE):self.assertIn(f'{axis}: {canonical}',text)
            self.assertIn(f'{labels[axis]}: `[select one: {" | ".join(values)}]`',CHARTER)
    def test_no_fabricated_behavior_evidence(self):
        self.assertIn('not transcripts, testimonials, external evidence, or proof of live-host or model behavior',FIRST)
if __name__=='__main__':unittest.main()
