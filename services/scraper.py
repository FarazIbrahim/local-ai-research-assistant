from newspaper import Article

def extract_text(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text
        return text[:3000]

    except Exception:
        return ""
