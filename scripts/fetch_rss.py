"""
Script for fetching RSS feeds and parsing article data.
"""
import feedparser

def fetch_rss(feed_urls):
    """
    Fetch and parse RSS feeds.

    Args:
        feed_urls (list of str): List of RSS feed URLs.

    Returns:
        list of dict: Parsed articles with metadata (title, link, summary).
    """
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.get('summary', ''),
            })
    return articles

if __name__ == "__main__":
    # Example feed URLs
    feed_urls = [
        "https://openai.com/rss",
        "https://www.anthropic.com/index.xml",
        "https://venturebeat.com/category/ai/feed/",
    ]

    # Fetch and print articles
    articles = fetch_rss(feed_urls)
    for article in articles:
        print(f"Title: {article['title']}\nLink: {article['link']}\nSummary: {article['summary']}\n")