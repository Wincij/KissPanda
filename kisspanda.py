
from bs4 import BeautifulSoup
import requests

def getDirectVideoLink(page):
    request = requests.get(page)
    html = request.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    videoLink = soup.find('div', class_="post-single-content box mark-links")
    videoLink = videoLink.p
    videoLink = videoLink.find('iframe')['src']
    return videoLink


info ="Dear kisspanda.net! It's really annoying when you turn on mining scripts without even informing us. Here I get all direct links to videos you have embeded.\nHave a nice day xD"


print(info)
print("Enter direct link to KissPanda.net page: ")
series = input()
# series = 'http://www.kisspanda.net/family-guy-watch-online/'
request = requests.get(series)

html = request.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

seasons = soup.find_all('ul', class_="listings episodeListings")

list = []
for season in seasons:
    episodes = season.find_all('li')
    for episode in episodes:
        link = episode.a['href']
        directViedoLink = getDirectVideoLink(link)
        print(directViedoLink)
        list.append(directViedoLink)





print("Write to file? [Y/n]")
write = input()


if write == 'Y':
    try:
        f = open("episodes.txt", "a")

    except:
        print("Error while writing file")


    for episode in list:
        f.write(episode+"\n")
