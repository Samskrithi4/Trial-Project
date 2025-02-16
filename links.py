import requests
from bs4 import BeautifulSoup

def getLinks(url):
    response = requests.get(url)

    #scrape the main website - List of films wikipedia page
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")

    allLinks = soup.find('table', class_='wikitable').find_all("a", href=True)
    allLinks = [a_tag['href'] for a_tag in allLinks]

    # collect links that are categorized by title (27 from 'A' to '0-9')
    allLinksSet = sorted(set(allLinks))
    return allLinksSet
    

if __name__ == '__main__':
    print("hello")
    url = "https://en.wikipedia.org/wiki/Lists_of_films"
    
    links = getLinks(url)
    
    with open("url.txt", 'w') as outfile:
        for link in links:
            outfile.write("https://en.wikipedia.org" + link + "\n")