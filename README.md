# Doctoral Thesis Pipeline

`doctoral-thesis-pipeline` is a Codex skill for stage-gated doctoral proposal and thesis drafting.

It helps turn incomplete thesis ideas into coherent academic deliverables while preserving truthfulness, traceability, and alignment across the research backbone.

## Best Fit

This skill is designed for PhD, DBA, and EdD work that needs:

- topic refinement
- proposal drafting
- literature review structuring
- methodology planning
- revision support
- gate-based quality checks

It is especially useful when a user has a promising topic but the title, research questions, variables, framework, and method are still not aligned.

## Core Principles

- Do not fabricate citations, findings, coefficients, or sample statistics
- Prefer narrowing scope over forcing weak completeness
- Align title, gap, framework, variables, and method before expanding prose
- Build a traceable literature base before writing from memory on current or niche topics
- Produce files, not just advice, when thesis work product is needed

## Workflow

The skill treats thesis support as an execution problem, not just a writing problem:

1. Classify the thesis stage
2. Normalize the research backbone
3. Build the minimum literature base
4. Draft the stage-specific deliverable
5. Run hard and soft gate checks before calling the result usable

## Supported Thesis Stages

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

## Typical Deliverables

Depending on the user request, the skill can help produce:

- refined title options
- research gap statements
- proposal chapters 1-3
- hypotheses or propositions
- methodology plans
- revision matrices
- literature retrieval files

It is designed to work well with practical output files such as:

- `project_config.yaml`
- `research_plan.md`
- `references/query_plan.md`
- `references/candidate_papers.jsonl`
- `references/evidence_table.csv`
- `outputs/proposal_draft.md`
- `outputs/revision_matrix.md`

## Repository Layout

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

## Included References

- `references/proposal-workflow.md`
  Proposal-stage structure, logic chain, chapter expectations, and common failure modes
- `references/literature-retrieval.md`
  Search strategy, evidence extraction rules, and retrieval outputs
- `references/gates.md`
  Hard and soft completion gates

## Included Script

`scripts/semantic_scholar_search.py` helps create a seed literature pool when `SEMANTIC_SCHOLAR_API_KEY` is available.

Example:

```bash
python scripts/semantic_scholar_search.py --query "AI tourism marketing" --limit 20 --out candidate_papers.jsonl
```

You can provide the API key through the process environment or `.env.local`.

## Related Skills

This skill is designed to work especially well with:

- `figures-diagram` for conceptual frameworks, methodology diagrams, taxonomy diagrams, flowcharts, and other non-numeric academic figures

## Installation

Copy this folder into your Codex skills directory:

```text
$CODEX_HOME/skills/doctoral-thesis-pipeline
```

On Windows, this is typically:

```text
C:\Users\<your-user>\.codex\skills\doctoral-thesis-pipeline
```

## Example Usage

- `Use $doctoral-thesis-pipeline to turn my rough topic into proposal chapters 1-3.`
- `Use $doctoral-thesis-pipeline to strengthen the logic of my methodology section.`
- `Use $doctoral-thesis-pipeline to create a literature review workflow and evidence table.`
- `Use $doctoral-thesis-pipeline to revise my proposal after supervisor feedback.`

## Who This Repository Is For

- Codex users who want a reusable thesis skill
- academic writing workflow builders
- researchers who want a structured proposal pipeline instead of ad hoc prompting

## License

MIT
