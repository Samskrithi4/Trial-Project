import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from sys import argv

def scrape(url):

    language_counts = defaultdict(int)

    if url.find("/wiki/") == -1:
        return language_counts
  #  url_link="https://en.wikipedia.org" + url
    url_link = url
    sub_response = requests.get(url_link,)

    # add the links to url to avoid repeating the same webpages
    # if url_link not in url:
    # url.append(url_link)
    #     else:
    #         continue

    sub_soup = BeautifulSoup(sub_response.content, 'html.parser')
    title = sub_soup.find(id="firstHeading")
    #print(title.string)
    subLinkOuter = sub_soup.find('div', class_='mw-content-ltr mw-parser-output')
    subLinkInner = subLinkOuter.find_all('div', class_='div-col')

    if subLinkInner:
        subLinks = []
        for link in subLinkInner:
            tempLink = link.find_all('a', href=True)
            subLinks.extend([a_tag['href'] for a_tag in tempLink])

        # movie names
        subLinksSet = sorted(set(subLinks))

        for subLink in subLinksSet:
            if subLink.find("/wiki/") == -1:
                continue 
            test_link = "https://en.wikipedia.org" + subLink

            resp = requests.get(test_link,)
            # add the links to url to avoid repeating the same webpages
            # if test_link not in subLinks:
            #     subLinks.append(test_link)
            # else:
            #     continue

            print(test_link)
            sp = BeautifulSoup(resp.content, 'html.parser')
            ti = sp.find(id="firstHeading")
            #print(title.string)
            inLink = sp.find('div', id='mw-content-text')
            tags = inLink.find_all('tr')

            lng = [tag for tag in tags if "language" in tag.text.lower()]
            for fin in lng:
                final_tag = fin.find('td')
                if final_tag is None:
                    continue
                text = final_tag.text.lower()
                #print(text)
                language_counts[text] += 1

   # print(language_counts)
    sorted_items = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
    top_10 = dict(sorted_items[:10])
    return top_10
            
    #print(subLinks)

#print(len(url)) # length should be 28
#print(url)

if __name__ == '__main__':
    print("hello")
    if len(argv) == 3:
        print(argv[1])
        url = argv[1]
        language_counts = scrape(url)
        print(f"Language counts for {url}:")
        print(language_counts)
        print()
       # with open(file_path, 'r') as file:
            # urls = file.readlines()
            # for url in urls:
            #     url = url.strip()  # Remove leading/trailing whitespaces and newlines
            #     print(url)
            #     language_counts = scrape(url)
            #     print(f"Language counts for {url}:")
            #     print(language_counts)
            #     print()
                
#                 for language, count in language_counts.items():
#                     total_language_counts[language] += count
#         print("Total Language counts:")
#         print(total_language_counts)
    else:
        print("failed")