import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for story_heading in soup.find_all(class_="e1voiwgp0"):
    if story_heading.span:
        print(story_heading.span.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())