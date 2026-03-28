---
name: doctoral-thesis-pipeline
description: Stage-gated workflow for doctoral proposals and thesis drafting. Use when Codex needs to turn rough thesis information into structured academic deliverables such as topic refinement, proposal chapters, literature reviews, methodology sections, revision plans, or thesis-progress workflows. Especially useful for PhD, DBA, and EdD work that needs research-question tightening, theory-method alignment, literature retrieval, gate-based quality control, and draft generation without fabricating citations or results.
---

# Doctoral Thesis Pipeline

## Overview

Use this skill to convert incomplete thesis inputs into a coherent academic workflow and draft package. Prioritize logical alignment across title, research questions, theory, variables, methods, evidence, and chapter outputs.

Treat thesis support as an execution problem, not just a writing problem:

1. Normalize the research design.
2. Build the minimum literature base.
3. Draft the stage-specific deliverable.
4. Run gate checks before calling the section usable.

## Core Rules

Follow these rules in order:

1. Preserve truthfulness and traceability.
2. Do not fabricate citations, statistics, coefficients, sample sizes, or findings.
3. Prefer narrowing scope over forcing completeness.
4. Keep the title, research questions, model, variables, and method aligned.
5. Produce files, not just advice, whenever the user is asking for thesis work product.

Pause only when continuing would require fabrication, incompatible assumptions, or missing mandatory inputs.

## Workflow

### 1. Classify the thesis stage

Map the user request to one of these stages:

- Topic selection
- Proposal
- Literature review
- Methodology
- Data collection
- Data analysis
- Full draft
- Revision
- Final submission
- Viva preparation

If the stage is ambiguous, infer it from the current deliverable. For example:

- "Help me tighten the logic" usually means proposal or revision.
- "Write the first three chapters" usually means proposal.
- "I already tested the model" usually means methodology or proposal with preliminary analysis.

### 2. Normalize the research backbone

Before writing long sections, lock these items:

- Working title
- Research problem
- Research questions
- Theoretical framework
- Core variables or constructs
- Unit of analysis
- Intended method

If any of these conflict, repair the alignment first. Do not let a proposal proceed with mismatched title, variables, and method.

For proposal-stage work, read [references/proposal-workflow.md](./references/proposal-workflow.md).

### 3. Build a minimal literature base

Do not write a literature review from memory when the topic is current or niche. Build a small but traceable literature base first.

For literature retrieval:

1. Generate 4 query types:
   - topic
   - method
   - mechanism
   - counterargument or neighboring literature
2. Retrieve from at least one credible source.
3. De-duplicate by DOI first, then by title plus author plus year.
4. Extract only what is needed to support the current stage.

When Semantic Scholar access is available, use [scripts/semantic_scholar_search.py](./scripts/semantic_scholar_search.py).

For retrieval rules and output files, read [references/literature-retrieval.md](./references/literature-retrieval.md).

### 4. Draft the stage-specific deliverable

Produce the smallest complete deliverable that matches the stage.

Typical outputs:

- Topic selection:
  - refined title options
  - research gap statement
  - preliminary framework
- Proposal:
  - chapters 1-3 draft
  - hypotheses or propositions
  - method plan
  - ethics notes
- Literature review:
  - thematic synthesis
  - gap map
  - concept-to-citation matrix
- Methodology:
  - variable table
  - sampling plan
  - instrument design
  - analysis plan
- Revision:
  - issue list
  - revision matrix
  - rewritten sections

When the thesis deliverable would benefit from non-numeric figures such as conceptual frameworks, process flowcharts, methodology diagrams, taxonomy charts, or timelines, prefer using the `$figures-diagram` skill to generate polished English diagram prompts and, when requested, render draft figures.

When possible, create practical files such as:

- `project_config.yaml`
- `research_plan.md`
- `references/query_plan.md`
- `references/candidate_papers.jsonl`
- `references/evidence_table.csv`
- `outputs/proposal_draft.md`
- `outputs/revision_matrix.md`

### 5. Run gates before calling it done

Use hard gates and soft gates.

Hard gates:

- no fabricated evidence
- no broken title-model-method alignment
- no unsupported core claim
- no missing mandatory section for the current stage

Soft gates:

- length targets
- citation-count targets
- breadth of literature
- polish and formatting depth

If a hard gate fails, stop and repair it. If a soft gate fails, note it and continue when appropriate.

For the full gate model, read [references/gates.md](./references/gates.md).

## Proposal Mode

When the user is at proposal stage:

1. Rewrite the topic into an academically defensible title.
2. Translate rough ideas into research questions.
3. Convert broad claims into a theory-backed model.
4. Add hypotheses or propositions if the method is quantitative or explanatory.
5. Draft the first three chapters as a coherent package:
   - Introduction
   - Literature Review
   - Methodology

Do not let the proposal drift into disconnected sections. The proposal should answer one continuous chain:

`why this problem matters -> what the literature misses -> what model explains it -> how the study will test it`

When proposal-stage chapters need a conceptual framework figure, research process flowchart, chapter structure diagram, or any other non-numeric academic diagram, prefer `$figures-diagram` instead of describing the figure vaguely in prose.

## Literature Review Mode

When the user asks for a literature review:

1. Identify themes, not just paper summaries.
2. Separate background literature from mechanism literature.
3. Include supporting and competing views when available.
4. End with an explicit gap statement.

A good review should tell the reader why the new study exists, not just prove the writer has read papers.

## Methodology Mode

When the user asks for methodology:

1. Match method to research question and variable type.
2. State sampling logic clearly.
3. Separate constructs, indicators, and observed variables.
4. Explain why each method step is necessary.
5. Include ethics handling when human subjects are involved.

Do not propose advanced analysis just to sound rigorous. Prefer the simplest defensible design.

## Revision Mode

When the user provides supervisor feedback or says the logic is weak:

1. Diagnose whether the problem is conceptual, structural, evidential, or stylistic.
2. Fix the backbone first.
3. Rewrite sections after the structure is repaired.

Typical revision order:

1. title and research questions
2. framework and hypotheses
3. literature gap
4. methods logic
5. wording and formatting

## Writing Guidance

Keep the prose academic but not bloated.

Avoid:

- empty claims like "many scholars believe"
- generic significance inflation
- list-like paper summaries with no synthesis
- variables that appear in one chapter but disappear in the next

Prefer:

- direct claims tied to named sources
- paragraph-level synthesis
- explicit transitions from literature to gap to model
- precise language about scope and limitation

## Resources

### references/

Load these only when needed:

- [references/proposal-workflow.md](./references/proposal-workflow.md)
  Use for proposal-stage structure, alignment rules, and deliverables.
- [references/literature-retrieval.md](./references/literature-retrieval.md)
  Use for search strategy, evidence extraction, and retrieval outputs.
- [references/gates.md](./references/gates.md)
  Use for hard and soft gate checks and stage-based completion rules.

### scripts/

- [scripts/semantic_scholar_search.py](./scripts/semantic_scholar_search.py)
  Use to create a seed literature pool when `SEMANTIC_SCHOLAR_API_KEY` is available.
