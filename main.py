from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.parent.name)
# print(soup.get_text())

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = (soup.find_all(name="a", class_="titlelink"))
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

# upvotes = []
# article_upvotes = soup.find_all(name="span", class_="score")
# for upvote in article_upvotes:
#     upvote =
#     upvotes.append(upvote)
upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

# for article_tag in  article_tages:
#     print(article_tag.text)

print(article_texts)
print(article_links)
print(upvotes)