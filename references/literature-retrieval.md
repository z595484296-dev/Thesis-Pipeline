# Literature Retrieval

## Purpose

Use this guide when the thesis work needs a current or traceable literature base.

## Retrieval Principle

Do not write from memory when the topic is current, specific, or method-sensitive. Retrieve first, then write.

## Query Types

Generate at least these query families:

1. Topic query
2. Method query
3. Mechanism query
4. Neighboring or counterargument query

## OpenScholar-Lite Pattern

Use a lightweight retrieval workflow:

1. Generate queries.
2. Retrieve papers.
3. De-duplicate.
4. Rank by relevance.
5. Extract evidence.
6. Write from evidence, not from titles alone.

## Minimum Output Files

Prefer creating:

- `references/query_plan.md`
- `references/retrieval_log.jsonl`
- `references/candidate_papers.jsonl`
- `references/evidence_table.csv`
- `references/reading_notes.md`

## Evidence Extraction

For each strong paper, capture:

1. What problem it studies
2. What method it uses
3. What variables or constructs matter
4. What its main finding is
5. Why it matters for the current thesis

## Caution

Do not treat every retrieved paper as usable evidence.

Weak evidence:

- title only
- no abstract
- unclear source
- no DOI or stable identifier
- irrelevant neighboring domain

Strong evidence:

- direct topic match
- clear abstract
- identifiable source
- usable for theory, method, or mechanism

## Semantic Scholar Script

If `SEMANTIC_SCHOLAR_API_KEY` is available, use `scripts/semantic_scholar_search.py` to create a first-pass candidate set.
