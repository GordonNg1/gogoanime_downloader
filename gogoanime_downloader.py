import requests
from bs4 import BeautifulSoup

URL = "https://gogoanimehd.to/detective-conan-remastered-episode-1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="dowloads")

#downloadLink = soup.find_all(text="Detective+Conan+Remastered")
downloadLink = results.find("a", href=True)
downloadUrl = downloadLink['href']
print(downloadUrl)

parent = downloadLink.parent()



# print(downloadLink)
