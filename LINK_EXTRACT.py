# https://en.wikipedia.org/wiki/Programmer


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
import time

def extract(Domain):
    try:
        response = requests.get(Domain)
        response.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException:
        print(f"Error fetching {Domain}")
        return []
    soup=BeautifulSoup(response.content,'html.parser')
    extract_urls=set()
    # base_domain='/'.join(Domain.split('/')[:3])
    for link in soup.find_all("a"):
        href=link.get("href")
        if href:
            full_url=urljoin(Domain,href)
            extract_urls.add(full_url)
    return extract_urls

def crawl(Domain):
    to_visit=set([Domain])
    visited=set()
    all_urls=set()
    max_depth=3
    depth=0
    while to_visit and depth<max_depth:

        # new_url=set()
        current_url=to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            new_url=extract(current_url)
            to_visit.update(new_url)#-visited)
            all_urls.update(new_url)
            time.sleep(0.5)
        depth +=1

    return all_urls


Domain=input("Enter your link: ")
# stors(link)
urls= crawl(Domain)
# print(urls)
for url in urls:
    print(url)