import cloudscraper
import os
import time
from lxml import html
from .logger import logger as log

def tree_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    tree = html.fromstring(content)
    return tree

def scrape(url, filepath, overwrite=False, timeout=(3,7)):
    log.LogDebug(f'scrape {url}')
    if not overwrite and os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return html.fromstring(f.read())
    while True:
        scraper = cloudscraper.create_scraper()
        try:
            scraped = scraper.get(url, timeout=timeout)
        except Exception as e:
            log.LogDebug("scrape error %s" % e)
        if scraped.status_code < 400:
            break
        else:
            log.LogDebug("HTTP error %s" % scraped.status_code)
        time.sleep(2)
    
    with open(filepath, 'wb') as f:
        f.write(scraped.content)
    return html.fromstring(scraped.content)