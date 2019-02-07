from urllib.request import Request, urlopen
import ssl

unverified_context = ssl._create_unverified_context()

response = Request("http://www.pokerscout.com", headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(response).read()

f = open("pokerscout.html","wb")

f.write(page)  

f.close()