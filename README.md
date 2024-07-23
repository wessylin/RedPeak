# RedPeak Global
**RedPeak Global (kyu Collective) x Wesley <Internship 2024>**
_________________________________________________________________________________________________________________________________________________________________________________________

GitHub Repository: https://github.com/wessylin/RedPeak

Future Projects (brainstorming):
1. AI Ecosystem & AI PC Trends
2. Competitor Outlook
3. Consumer Trends

** IFA GPC (Global Press Conference)
_________________________________________________________________________________________________________________________________________________________________________________________

**(COMPLETED) Amazon Product Review Scraper/Analyzer**
- Associated client projects: Acer PAP, Acer AI PC, multi-purpose
- (WORKING) ImportFromWeb x GPT Extension 
  - A useful AI tool combining “ImportFromWeb” and GPT for sheets to automatically scrape product reviews on Amazon, and conduct a general sentiment analysis.
- (WORKING/BEST) Sentiment Analyzer - Vader
  - vader_wes.py is a specialized AI tool that filters and sorts Amazon reviews and performs sentiment analysis on them. It leverages the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer to assess the reviews' tone, word choice, use of emojis, punctuation, capitalization, and other textual elements. The tool generates a compound score for each review, which is then graphed for better visualization during strategy planning and client presentations.
  - How it works:
    - The sentiment analyzer uses the VADER NLP model, which employs a dictionary of words and rules to determine the sentiment of a text. After tokenization and segmentation, each word is assigned a valence score reflecting its positivity or negativity. The overall sentiment of the review is then computed based on these scores.
  - Instructions:
    - Use a Google Chrome extension to export the desired Amazon reviews of a product into a CSV file.
    - Indicate the path to the CSV file in the vader_wes.py script.
    - Execute the script to perform the sentiment analysis and generate the compound score graph.
- Source of Inspiration: [https://www.youtube.com/watch?v=QpzMWQvxXWk&ab_channel=RobMulla](url)
__________________________________________________________________________________________________________________________________________________________________________________

**(COMPLETED) Google Search Result Web Crawler**
- Associated client projects: Acer PAP, Acer AI PC, multi-purpose
- Progress:
  - (WORKING) ogCrawler:
    - (WORKING) Version 0: iter_title.py
      - Successfully scrapes the titles of the top search results on Google
    - (SCRATCHED) Version 1: iter_plus.py 
      - Scratched attempt at scraping the title and URL of the top search results on Google
    - (WORKING/BEST) Version 2: iter_parse.py
      - Successfully scrapes the titles of the top search results on Google and its URL
    - (PAUSED) Version 3: iter_news.py
  - (WORKING/BEST) Advanced Oxylabs x Postman Crawler
    - An advanced SERP scraper API combining Oxylabs and Postman specialized in search result crawling.
    - Capabilities:
      1. Geo-Location
      2. Search Engine
      3. Dates (before - after)
      4. Page specification 
- Comments: 
  - ogCrawler is written completely from scratch (proprietary to RedPeak x Wesley)
  - Future use of Oxylabs may not be free, not expensive either, however, it is important to note its web data-gathering capabilities can be very worth it.


_________________________________________________________________________________________________________________________________________________________________________________________

**(PAUSED) Dynamic Web to Text Crawler**
  - Associated Client Projects: Acer PAP, Acer AI PC, multi-purpose
  - Progress
    - (PAUSED) Dynamic2Text 
      - Dynamic2Text attempts to crawl from a given list of dynamic websites and retrieve the desired texts/content.  
      - productSpider.py can successfully crawl the given list of websites and automatically save certain information from each website into distinct HTML files, however, currently, the information retrieved is more inconsistent the more dynamic the website becomes.
      - Challenges faced:
        1. Some dynamic websites employ robot.txt, an exclusion protocol that prevents crawlers from accessing web content.
        2. Most of the tech websites we are trying to crawl are dynamic rather than static, adding a layer of complexity to making a high-value crawler. 
      - Next steps:
        - Integrate Selenium into Dyanmic2Text. Selenium can support browser automation and mimic human activity. 
    - (GOOD ALTERNATIVE) All-In-One with Jina AI - Search & RAG Solutions
      - Jina AI x RedPeak AI Tool: [https://docs.google.com/document/d/1k3H9iOWHVyGHZImtjUyn9eKek3k-dEsq_ZSTa0yGVa8/edit?usp=sharing](url)

- Comments:
  - By combining ogCrawler and Dynamic2Text, we can autonomize the first steps of strategy research from search to data consolidation. 
_________________________________________________________________________________________________________________________________________________________________________________________

Reference Resources: 
[https://github.com/gokseltokur/Social-Media-Sentiment-Analysis
](URL)

Useful Commands:
python3 -m venv webcrawl
source webcrawl/bin/activate 
Chromedriver path: /Users/wesleylin/PAP/chrome-headless-shell-mac-x64
curl 'https://realtime.oxylabs.io/v1/queries' --user 'redaipc_isCyz:Redpeak123' -H 'Content-Type: application/json' -d '{"source": "google_search", "domain": "com", "query": "adidas", "geo_location": "Taipei, Taiwan", "parse": true}'
