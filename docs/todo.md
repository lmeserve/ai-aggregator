# AI Aggregator - To-Do List

## Phase 1: Setup
- [x] Create repository with README, LICENSE, and .gitignore
- [ ] Define the initial list of 10 AI RSS Feeds
- [ ] Create placeholder scripts for the following:
    - [ ] Fetching RSS Feeds
    - [ ] Scraping Content
    - [ ] Relevance Checking
    - [ ] HTML Slide Deck Generation

## Phase 2: RSS & Scraping
- [ ] Use `feedparser` for RSS data retrieval.
- [ ] Extract summaries and links from feeds.
- [ ] Handle edge cases where articles are insufficiently described in RSS.

## Phase 3: Relevance Checking
- [ ] Define keywords for filtering.
- [ ] Use basic ML model if possible (e.g., Naive Bayes).

## Phase 4: HTML Presentation
- [ ] Design slide layout in HTML.
- [ ] Use `jinja2` templates for rendering.

## Phase 5: Scheduling
- [ ] Implement a GitHub Action workflow.
    OR
- [ ] Deploy as an Azure Function (optional).