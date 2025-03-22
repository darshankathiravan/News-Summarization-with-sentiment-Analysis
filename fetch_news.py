import requests
from bs4 import BeautifulSoup

def extract_topics(article_url):
    try:
        response = requests.get(article_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        if response.status_code != 200:
            return ["No topics found"]

        soup = BeautifulSoup(response.text, "html.parser")

        meta_keywords = soup.find("meta", {"name": "keywords"})
        if meta_keywords and meta_keywords.get("content"):
            return meta_keywords["content"].split(",")

        return ["No topics found"]
    
    except Exception:
        return ["Error extracting topics"]

def fetch_news(company_name):
    search_url = f"https://www.google.com/search?q={company_name}+news&tbm=nws"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return {"Company": company_name, "Articles": [{"Title": "Error fetching news", "Content": "Could not access Google News", "Topics": ["N/A"]}]}

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for result in soup.find_all("div", class_="SoaBEf")[:10]:  # Get top 10 articles
        title_tag = result.find("div", class_="nDgy9d")
        snippet_tag = result.find("div", class_="GI74Re")
        link_tag = result.find("a")

        title = title_tag.get_text(strip=True) if title_tag else "No title found"
        content = snippet_tag.get_text(strip=True) if snippet_tag else "No content available"
        
        link = link_tag["href"] if link_tag and "href" in link_tag.attrs else None
        
        if link and link.startswith("/url?q="):
            link = link.split("/url?q=")[1].split("&")[0]  # Extract clean URL

        # Extract topics if the article link exists
        topics = extract_topics(link) if link and link.startswith("http") else ["No topics found"]

        articles.append({
            "Title": title,
            "Content": content,
            "Topics": topics
        })

    return {"Company": company_name, "Articles": articles}

# Example usage
if __name__ == "__main__":
    company = "Tesla"
    news_data = fetch_news(company)
    print(news_data)
