# RedPeak
RedPeak x Wesley <Internship 2024>

GitHub Repository: https://github.com/wessylin/RedPeak

Future Projects (brainstorming):
1. Social media sentiment analysis
2. AI Ecosystem & AI PC Trends
3. Competitor Outlook
4. Consumer Trends

** IFA GPC (Global Press Conference)
_________________________________________________________________________________________________________________________________________________________________________________________

(COMPLETED) Amazon Product Review Scraper/Analyzer
A useful AI tool combining “ImportFromWeb” and GPT for sheets to automatically scrape product reviews on Amazon, and conduct a general sentiment analysis.
_________________________________________________________________________________________________________________________________________________________________________________________

(COMPLETED) Google Search Result Web Crawler
Associated Client Projects: Acer PAP, Acer AI PC, multi-purpose
Progress:
ogCrawler (Week 1/2):
(WORKING) Version 0: iter_title.py 
Successfully scrapes the titles of the top search results on Google
(SCRATCHED) Version 1: iter_plus.py 
Scratched attempt at scraping the title and URL of the top search results on Google
(WORKING/BEST) Version 2: iter_parse.py
Successfully scrapes the titles of the top search results on Google and its URL
Has an option 
(PAUSED) Version 3: iter_news.py
(WORKING/BEST) Advanced Oxylabs x Postman Crawler (Week 2)
An advanced SERP scraper API combining Oxylabs and Postman specialized in search result crawling.
Capabilities:
Geo-Location
Search Engine
Dates (before - after)
Page specification 
Comments: 
ogCrawler is written completely from scratch (proprietary to RedPeak x Wesley)
Future use of Oxylabs may not be free, not expensive either, however, it is important to note its web data-gathering capabilities can be very worth it.

(PAUSED) Dynamic Web to Text Crawler
Associated Client Projects: Acer PAP, Acer AI PC, multi-purpose
Progress
Dynamic2Text (PAUSED - Week 1) 
Dynamic2Text attempts to crawl from a given list of dynamic websites and retrieve the desired texts/content.  
productSpider.py can successfully crawl the given list of websites and automatically save certain information from each website into distinct HTML files, however, currently, the information retrieved is more inconsistent the more dynamic the website becomes.
Challenges faced:
Some dynamic websites employ robot.txt, an exclusion protocol that prevents crawlers from accessing web content.
Most of the tech websites we are trying to crawl are dynamic rather than static, adding a layer of complexity to making a high-value crawler. 
Next steps:
Integrate Selenium into Dyanmic2Text. Selenium can support browser automation and mimic human activity. 

(GOOD ALTERNATIVE) All-In-One with Jina AI - Search & RAG Solutions
Jina AI x RedPeak AI Tool


Comments:
By combining ogCrawler and Dynamic2Text, we can automize the first steps of strategy research from search to data consolidation. 



(NEXT) Social Media Sentiment Analyzer
Associated Client Projects: Acer PAP, Acer AI PC


Reference Resources: 
https://github.com/gokseltokur/Social-Media-Sentiment-Analysis

Useful Commands:
python3 -m venv webcrawl
source webcrawl/bin/activate 
Chromedriver path: /Users/wesleylin/PAP/chrome-headless-shell-mac-x64
curl 'https://realtime.oxylabs.io/v1/queries' --user 'redaipc_isCyz:Redpeak123' -H 'Content-Type: application/json' -d '{"source": "google_search", "domain": "com", "query": "adidas", "geo_location": "Taipei, Taiwan", "parse": true}'
