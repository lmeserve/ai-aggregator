"""
Unit tests for fetching RSS feeds with pytest.
"""
import pytest
import tempfile
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
    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_feed_file:
        temp_feed_file.write("http://mockfeed.com/rss\n")
        temp_feed_file_path = temp_feed_file.name

    results = fetch_rss(temp_feed_file_path)

    assert len(results) == 2
    assert results[0]["title"] == "Test Title 1"
    assert results[0]["link"] == "http://example.com/1"
    assert results[0]["summary"] == "Summary 1"
    assert results[1]["title"] == "Test Title 2"
    assert results[1]["link"] == "http://example.com/2"
    assert results[1]["summary"] == "Summary 2"