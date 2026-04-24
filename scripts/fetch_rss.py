"""
Script for fetching RSS feeds and parsing article data.
"""
import feedparser
import json

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

def save_articles_to_file(articles, output_file):
    """
    Save the fetched articles to a JSON file.

    Args:
        articles (list of dict): List of article data parsed from RSS feeds.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, "w") as file:
            json.dump(articles, file, indent=4)
        print(f"Articles saved to {output_file}")
    except Exception as e:
        print(f"Error saving articles to file: {e}")

if __name__ == "__main__":
    # Path to RSS feed file
    feed_file_path = "data/rss_feeds.txt"
    output_file = "data/fetched_articles.json"

    # Fetch articles
    articles = fetch_rss(feed_file_path)

    # Save articles to file
    save_articles_to_file(articles, output_file)