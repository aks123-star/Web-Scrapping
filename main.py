import bs4
import requests

res= requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = bs4.BeautifulSoup(res.text,'html.parser')
filename = "temp.html"
# soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text)
for link in soup.find_all('a',href=True):
    print(link['href'])


formatted_text = soup.prettify()
with open (filename , "w+") as f:
    f.write (formatted_text)