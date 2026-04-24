"""
Unit tests for fetching RSS feeds with pytest.
"""
import pytest
from scripts.fetch_rss import fetch_rss

@pytest.fixture
def mock_feedparser(mocker):
    """
    Mock the feedparser.parse function.
    """
    def mock_parse(url):
        return {
            "entries": [
                {"title": "Test Title 1", "link": "http://example.com/1", "summary": "Summary 1"},
                {"title": "Test Title 2", "link": "http://example.com/2", "summary": "Summary 2"}
            ]
        }
    return mocker.patch("feedparser.parse", side_effect=mock_parse)

def test_fetch_rss(mock_feedparser):
    """
    Test the fetch_rss function to ensure it correctly processes articles.
    """
    feed_urls = ["http://mockfeed.com/rss"]
    results = fetch_rss(feed_urls)

    assert len(results) == 2
    assert results[0]["title"] == "Test Title 1"
    assert results[0]["link"] == "http://example.com/1"
    assert results[0]["summary"] == "Summary 1"
    assert results[1]["title"] == "Test Title 2"
    assert results[1]["link"] == "http://example.com/2"
    assert results[1]["summary"] == "Summary 2"