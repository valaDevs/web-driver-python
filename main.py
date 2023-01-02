from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.a)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))  # getting specific attributes

heading = soup.find(name="h1", id="name")  # get the first match or get with the ID
print(heading)

section_heading = soup.find(name="h3", class_="heading")  # class_

comapany_url = soup.select_one(selector="p a")  # css selector
comapany_url2 = soup.select_one(selector="#name")  # css selector
comapany_url3= soup.select(selector=".heading")  # css selector
print(comapany_url)