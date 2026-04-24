"""
Script for fetching RSS feeds and parsing article data.
"""
import feedparser

def fetch_rss(feed_file_path):
    """
    Fetch and parse RSS feeds.

    Args:
        feed_file_path (str): Path to the file containing RSS feed URLs.

    Returns:
        list of dict: Parsed articles with metadata (title, link, summary).
    """
    articles = []

    # Load feed URLs from a file
    try:
        with open(feed_file_path, "r") as feed_file:
            feed_urls = [line.strip() for line in feed_file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{feed_file_path}' not found.")
        return articles

    # Parse each feed URL
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
    # Path to RSS feed file
    feed_file_path = "data/rss_feeds.txt"

    # Fetch and print articles
    articles = fetch_rss(feed_file_path)
    for article in articles:
        print(f"Title: {article['title']}\nLink: {article['link']}\nSummary: {article['summary']}\n")