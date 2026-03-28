# Doctoral Thesis Pipeline

`doctoral-thesis-pipeline` is a Codex skill for stage-gated doctoral proposal and thesis drafting.

It is designed for PhD, DBA, and EdD work that needs:

- topic refinement
- theory-method alignment
- traceable literature retrieval
- proposal chapter drafting
- methodology planning
- revision support
- gate-based quality checks

The skill emphasizes truthfulness, traceability, and structural alignment across title, research questions, framework, variables, method, evidence, and chapter outputs.

## What This Skill Does

This skill helps Codex turn rough thesis inputs into structured academic deliverables such as:

- proposal chapters 1-3
- literature reviews
- methodology sections
- revision matrices
- thesis progress workflows

It is especially useful when a thesis topic is current, niche, or logically underdeveloped and the user needs a tighter academic backbone before expanding the draft.

## Repository Structure

```text
SKILL.md
agents/
  openai.yaml
references/
  gates.md
  literature-retrieval.md
  proposal-workflow.md
scripts/
  semantic_scholar_search.py
```

## Key Features

- Stage classification from topic selection to viva preparation
- Proposal-mode workflow for drafting Chapters 1-3
- Minimal literature-base construction before writing from memory
- Hard and soft gates to catch misalignment and unsupported claims
- Support for practical work products such as:
  - `project_config.yaml`
  - `research_plan.md`
  - `references/query_plan.md`
  - `references/candidate_papers.jsonl`
  - `references/evidence_table.csv`
  - `outputs/proposal_draft.md`

## Related Skills

This skill is designed to work especially well with:

- `figures-diagram` for conceptual frameworks, methodology diagrams, timelines, and other non-numeric academic figures

## Installation

Copy this folder into your Codex skills directory:

```text
$CODEX_HOME/skills/doctoral-thesis-pipeline
```

On Windows, that is typically:

```text
C:\Users\<your-user>\.codex\skills\doctoral-thesis-pipeline
```

## Usage

Call the skill from Codex with prompts such as:

- `Use $doctoral-thesis-pipeline to turn my rough topic into proposal chapters 1-3.`
- `Use $doctoral-thesis-pipeline to strengthen the logic of my methodology section.`
- `Use $doctoral-thesis-pipeline to create a literature review workflow and evidence table.`

## Semantic Scholar Script

The included script can help create a seed literature pool when `SEMANTIC_SCHOLAR_API_KEY` is available:

```bash
python scripts/semantic_scholar_search.py --query "AI tourism marketing" --limit 20 --out candidate_papers.jsonl
```

You can place the API key in the process environment or in `.env.local`.

## Design Principles

- Do not fabricate citations, findings, or sample statistics
- Prefer narrowing scope over forcing completeness
- Keep the research backbone aligned before expanding prose
- Produce files, not just advice, when the task calls for thesis work product

## Notes

- This repository contains the skill itself, not a full thesis project
- No software license has been added yet
