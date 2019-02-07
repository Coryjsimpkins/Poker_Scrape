from bs4 import BeautifulSoup

f = open("pokerscout.html", "r")
soup = BeautifulSoup(f.read(), 'html.parser')

results = soup.find_all('td', attrs={'id' : 'online'})

online = []

for r in results:
	#print(r.text)
	online.append(r.text)
print(online)

results = soup.find_all('td', attrs={'id' : 'cash'})

cash = []

for r in results:
	#print(r.text)
	cash.append(r.text)
print(cash)

results = soup.find_all('td', attrs={'id' : 'pokerSite'})

site = []

for r in results:
	#print(r.text)
	site.append(r.text)
print(site)