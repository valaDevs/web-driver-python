from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
anchor = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []

for article_tag in anchor:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvote = [for score in soup.find_all(name="span", class_="score").getText()]
print(article_texts)
print(article_links)
print(article_upvote)
