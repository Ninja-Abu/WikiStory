from bs4 import BeautifulSoup
import requests

story = ""
depth = 3
base_url = "https://en.wikipedia.org"
search = "/wiki/United_States"

for d in range(depth):
    topic = search[6:].replace("_"," ")
    print(topic)
    result = requests.get(base_url+search)
    page = BeautifulSoup(result.text, "html.parser")
    content = page.find(class_="mw-parser-output")
    search_para_parent = content.find("b", text=topic).parent
    all_links = search_para_parent.find_all("a")#[-1]['href']
    for l in all_links[::-1]:
        if l['href'][0] == '/' and '#' not in l['href']:
            search = l['href']
            break

    for line in search_para_parent.strings:
         story += line
    story += "\n"
    print(story)
    story = ""

#print(story)


#bold = content.find("b")
#parent_bold = bold.parent
#last_link = parent_bold.find_all("a")
#print("search=",last_link[-1]['href'])
