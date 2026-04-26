import requests
from bs4 import BeautifulSoup
def email_snatcher():
  request = requests.get(input('Enter the URL: '))
  soup = BeautifulSoup(request.content, 'html.parser')
  for link in soup.find_all('a'):
    if '@' in str(link.get('href')):
      print(link.get('href').replace('mailto:', ''))
email_snatcher()
