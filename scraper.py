import requests
from bs4 import BeautifulSoup

def fetch_news(company_name):
    """Scrapes news articles related to the given company."""
    
    search_url = f"https://news.google.com/search?q={company_name}&hl=en&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for article in soup.select("article"):
        title_elem = article.select_one("h3 a")
        link_elem = article.select_one("a")

        if title_elem and link_elem:
            title = title_elem.text.strip()
            link = "https://news.google.com" + link_elem["href"][1:]
            
            # Fetch article summary
            summary = fetch_article_summary(link)

            articles.append({"title": title, "link": link, "summary": summary})

        if len(articles) >= 10:  # Limit to 10 articles
            break

    return articles


def fetch_article_summary(url):
    """Extracts a short summary from the article content."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Summary not available"

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    summary = " ".join([p.text for p in paragraphs[:3]])  # First 3 paragraphs

    return summary

