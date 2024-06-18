import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

class ProductSpider(scrapy.Spider):
    name = 'productSpider'
    
    # List of URLs to crawl
    start_urls = [
        'https://www.asus.com/us/laptops/for-home/vivobook/asus-vivobook-s-15-s5507/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10, screenshot=True)

    def parse(self, response):

        # Extract text from specific tags
        paragraphs = response.xpath('//p//text()').getall()
        headings1 = response.xpath('//h1//text()').getall()
        headings2 = response.xpath('//h2//text()').getall()
        headings3 = response.xpath('//h3//text()').getall()
        headings4 = response.xpath('//h4//text()').getall()
        headings5 = response.xpath('//h5//text()').getall()
        headings6 = response.xpath('//h6//text()').getall()
        list_items = response.xpath('//li//text()').getall()
        other_texts = response.xpath('//span//text() | //div//text()').getall()

        # Combine all text content
        page_text = '\n'.join(paragraphs + headings1 + headings2 + headings3 + headings4 + headings5 + headings6 + list_items + other_texts)

        # Clean up the text
        page_text = ' '.join(page_text.split())

        # Print the text to console
        self.log(page_text)

        # Create a filename based on the URL
        url_parts = response.url.split("/")
        filename = f"{url_parts[2]}_{url_parts[-2]}.html"
        
        # Ensure the folder exists
        folder_path = os.path.join(os.getcwd(), 'html_files')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Full file path
        file_path = os.path.join(folder_path, filename)

        # Save the extracted content to an HTML file
        with open(file_path, 'wb') as f:
            f.write(page_content)

        self.log(f'Saved file {file_path}')