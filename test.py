import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com/search?q=%EB%84%A4%EB%AA%A8")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select("h3")
for link in links:
    title = link.text
    print(title)