import requests
import bs4

#prompts user for an search input
text = input('About what would you like to scrape?')
url = 'https://google.com/search?q=' + text

#pings google and parses through html
request_result = requests.get(url)
soup = bs4.BeautifulSoup(request_result.text, 'html.parser')

# print(soup)

#extracts values from specified headers 
heading_object = soup.find_all('h3') 
# link_object = soup.find_all('a')

n = 1

for h, l in heading_object, link_object: 
    print("------") 
    print('Title', n, ':', h.getText()) 
    print("------") 
    n += 1
    if n > 11:
        break