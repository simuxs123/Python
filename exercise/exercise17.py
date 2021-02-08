import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for story_heading in soup.find_all("article"):
    if story_heading:
        print(story_heading.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())