from bs4 import BeautifulSoup
import md_converter as md_conv
import requests
import json
import sys


title_class_name = "mw-page-title-main"
title_id_name = "firstHeading"
article_id_name = "mw-content-text"

converter = md_conv.md_converter()
settings  = json.load(open("settings.json","r"))


url = "https://en.wikipedia.org/wiki/Markdown" if len(sys.argv) == 1 else sys.argv[1]
urls = open("to_scrape.txt","r").read().split("\n") if settings["parse list"] else [url]


current_article = 1
for url in urls:
    soup      = BeautifulSoup(requests.get(url).text, 'lxml')

    article = soup.find(id=article_id_name).div
    title   = soup.find(id=title_id_name).text

    converter.add_title(title)
    converter.add_linebreak()
    converter.add_in_line("-----------------------")


    for section in article.contents:

        if   section.name == "h2" : converter.add_header(section.contents,2)
        elif section.name == "h3" : converter.add_header(section.contents,4)
        
        elif section.name == "ul" : pass
        elif section.name == "ol" : pass
        elif section.name == "tbody" or section.name == "table"     : pass

        elif section.name == "p" :
            converter.add_in_line("  \n")
            for sentence in section.contents:

                if   isinstance(sentence,str) : converter.add_in_line(sentence)
                elif sentence.name == "code"  : converter.add_code(sentence.contents)
                elif sentence.name == "b"     : converter.add_bold(sentence.contents)
                elif sentence.name == "i"     : converter.add_italic(sentence.contents)
                elif sentence.name == "a"     : converter.add_link(sentence)
                

        elif isinstance(section,str) or "style" in section.name or "rel" in section.name or "link" in section.name:pass      
        elif "thumb" in section.attrs["class"] and settings["media"]: converter.add_image(section.contents)


    print("finished "+str(current_article)+":   "+url.split("/wiki/")[1])
    with open("out/"+str(current_article)+".md","w",encoding="utf-8") as file:
        file.write(converter.md_str)
    current_article += 1

