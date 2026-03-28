import argparse
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path


SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
DEFAULT_FIELDS = [
    "paperId",
    "title",
    "authors",
    "year",
    "venue",
    "abstract",
    "citationCount",
    "externalIds",
    "url",
]


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def api_headers() -> dict:
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "Missing SEMANTIC_SCHOLAR_API_KEY. Put it in the process environment or .env.local."
        )
    return {
        "x-api-key": api_key,
        "Accept": "application/json",
        "User-Agent": "doctoral-thesis-pipeline/0.1",
    }


def search(query: str, limit: int) -> list[dict]:
    params = urllib.parse.urlencode(
        {"query": query, "limit": limit, "fields": ",".join(DEFAULT_FIELDS)}
    )
    request = urllib.request.Request(
        f"{SEMANTIC_SCHOLAR_URL}?{params}",
        headers=api_headers(),
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload.get("data", [])


def dedupe(papers: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for paper in papers:
        ext_ids = paper.get("externalIds") or {}
        doi = (ext_ids.get("DOI") or "").strip().lower()
        authors = paper.get("authors") or []
        first_author = (authors[0].get("name") or "").strip().lower() if authors else ""
        year = str(paper.get("year") or "")
        title = " ".join((paper.get("title") or "").lower().split())
        key = doi or f"{title}|{first_author}|{year}"
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(paper)
    return unique


def to_record(query: str, rank: int, paper: dict) -> dict:
    ext_ids = paper.get("externalIds") or {}
    return {
        "query": query,
        "rank": rank,
        "source": "semantic_scholar",
        "paper_id": paper.get("paperId"),
        "title": paper.get("title"),
        "authors": [a.get("name") for a in (paper.get("authors") or []) if a.get("name")],
        "year": paper.get("year"),
        "venue": paper.get("venue"),
        "abstract": paper.get("abstract"),
        "citation_count": paper.get("citationCount"),
        "doi": ext_ids.get("DOI"),
        "url": paper.get("url"),
        "external_ids": ext_ids,
    }


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search Semantic Scholar and write candidate papers as JSONL."
    )
    parser.add_argument("--query", required=True, help="Search query.")
    parser.add_argument("--limit", type=int, default=20, help="Number of papers to fetch.")
    parser.add_argument(
        "--out",
        default="candidate_papers.jsonl",
        help="Output JSONL path.",
    )
    parser.add_argument(
        "--env-file",
        default=".env.local",
        help="Optional dotenv-style file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv(Path(args.env_file))
    papers = dedupe(search(args.query, args.limit))
    rows = [to_record(args.query, idx, paper) for idx, paper in enumerate(papers, start=1)]
    write_jsonl(Path(args.out), rows)
    print(f"Wrote {len(rows)} records to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
