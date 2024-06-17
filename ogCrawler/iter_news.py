import requests
import bs4
from urllib.parse import urlparse
from urllib.parse import parse_qs

#prompts user for an search input
text = input('About what would you like to scrape?')
url = 'https://news.google.com/search?q=' + text

request_result = requests.get(url)
soup = bs4.BeautifulSoup(request_result.text, 'html.parser')

print(soup)

def extract_href(href):
    url = urlparse(href)
    query = parse_qs(url.query)
    if not ('q' in query and query['q'] and len(query['q']) > 0):
        return None
    return query['q'][0]

def extract_section(gdiv):
    # Getting our elements
    title = gdiv.select_one('h3')
    link = gdiv.select_one('a')
    description = gdiv.find('.BNeawe')
    return {
        # Extract title's text only if text is found 
        'Title': title.text if title else None,
        # 'Link': link['href'].strip('/url?q=') if link else None, #process links w/ brute force
        # 'Link': extract_href(link['href']) if link else None,
        'Description': description.text if description else None,
    }

def extract_results(soup):
    main = soup.select_one("#main")

    for gdiv in main.select('.g, .fP1Qef'):
        print(extract_section(gdiv))

# heading_object = soup.find_all('h3') 
# link_object = soup.find_all('a')

print(extract_results(soup))



    