# Scrape http://quotes.toscrape.com/ using beautifulsoup

import requests
import bs4

# res = requests.get('http://quotes.toscrape.com')

# print(res.text)

# soup = bs4.BeautifulSoup(res.text,'lxml')

# print(soup.select('.author'))

# authors = set()

# for name in soup.select(".author"):
#   authors.add(name.text)


# print(authors)

# quotes = []
# for quote in soup.select('.text'):
#   quotes.append(quote.text)

# print(quotes)

# soup.select('.tag-item')

# Scrape every page 1-10 pages

url = 'http://quotes.toscrape.com/page/'

# authors = set()

# for page in range(1,10):

#   page_url = url+str(page)
#   res = requests.get(page_url)
#   soup = bs4.BeautifulSoup(res.text, 'lxml')

#   for name in soup.select(".author"):
#     authors.add(name.text)

# print(authors)

# Scrape every page until no more pages

page_still_valid = True
authors = set()
page = 1
while page_still_valid:
  page_url = url+str(page)

  res = requests.get(page_url)

  if "No quotes found!" in res.text:
    break
  

  soup = bs4.BeautifulSoup(res.text, 'lxml')

  for name in soup.select('.author'):
    authors.add(name.text)

  page = page+1

print(authors)

