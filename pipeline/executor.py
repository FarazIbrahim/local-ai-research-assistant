from services.search import search
from services.scraper import extract_text

def run_pipeline(query: str, max_results: int = 3):
    results = search(query, max_results=max_results)

    collected = []

    for r in results:
        text = extract_text(r["url"])

        collected.append({
            "title": r["title"],
            "url": r["url"],
            "text": text
        })

    return collected
