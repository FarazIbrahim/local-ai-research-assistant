from services.search import search

results = search("vibe coding")

for r in results:
    print(r["title"], r["url"])
