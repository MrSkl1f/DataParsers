import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

url = "https://rda.ucar.edu/services/outlines.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
variable = soup.find_all('a')
i = 1
for tag in variable:
    url2 = "https://rda.ucar.edu/" + tag.get('href')
    req2 = requests.get(url2, headers)
    soup2 = str(BeautifulSoup(req2.content, 'html.parser'))
    if i != 1:
        f = open(f"{i}.txt", "w")
        f.write(soup2)
        f.close()
    i += 1

