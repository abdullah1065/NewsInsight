import requests
from bs4 import BeautifulSoup
import cloudscraper
from urllib.parse import urlparse

scraper = cloudscraper.create_scraper()


def scrape_urls(category_url):

    parsed_url = urlparse(category_url)
    main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    article_path = 'article'

    response  = scraper.get(category_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        subcategory_urls = []
        article_urls = set()
        for link in soup.find_all('a', href=True):
            url = link['href']

            if url.startswith(category_url) and article_path not in url:
                full_url = f"{main_url}{url}" if url.startswith('/') else url
                subcategory_urls.append(full_url)

        for subcategory_url in subcategory_urls:

            subcategory_response = scraper.get(subcategory_url)
            if subcategory_response.status_code == 200:
                sub_soup = BeautifulSoup(subcategory_response.content, 'html.parser')
                for sub_link in sub_soup.find_all('a', href=True):
                    sub_url = sub_link['href']
                    if f'/{article_path}/' in sub_url:
                        full_article_url = f"{main_url}{sub_url}" if sub_url.startswith('/') else sub_url
                        article_urls.add(full_article_url)

        return list(article_urls)

    else:
        print(f"Failed to access {url}: Status code {response.status_code}")
        return None

def scrape_article_data(url):
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            title = soup.find('h1').text.strip()
        except AttributeError:
            title = "Unknown Title"

        try:
            meta_description = soup.find('meta', {'name': 'description'})['content']
        except TypeError:
            meta_description = "No description available"
        
        try:
            author = soup.find('div', {'class': 'writter'}).text.strip()
        except AttributeError:
            author = "Unknown Author"

        try:
            date_section = soup.find('div', {'class': 'dateAndTime'})
            published_date = date_section.find('p').text.strip().split(': ')[1]
        except AttributeError:
            published_date = "Unknown Date"

        try:
            content = soup.find('div', {'class': 'dNewsDesc'}).text.strip()
        except AttributeError:
            content = "Content not available"

        return {
            'url': url,
            'title': title,
            'meta_description': meta_description,
            'author': author,
            'published_date': published_date,
            'content': content,
        }
        
    else:
        print(f"Failed to access {url}: Status code {response.status_code}")
        return None