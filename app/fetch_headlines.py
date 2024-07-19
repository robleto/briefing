# app/fetch_headlines.py
from newspaper import Article

def fetch_headlines(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title, article.text
