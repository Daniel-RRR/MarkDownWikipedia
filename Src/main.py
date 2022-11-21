from bs4 import BeautifulSoup
import md_converter as md_conv
import requests


url = "https://en.wikipedia.org/wiki/Slovakia"
title_class_name = "mw-page-title-main"
article_id_name = "mw-content-text"

# TODO : PICTURES
# TODO : LISTS
# TODO : JSON SETTINGS
# TODO : TOC
# TODO : TABLE

soup = BeautifulSoup(requests.get(url).text, 'lxml')
converter = md_conv.md_converter()

title = soup.find(class_=title_class_name).contents.pop(0)
article = soup.find(id=article_id_name).div

converter.add_title(title)
converter.add_linebreak()
converter.add_in_line("-----------------------")


for section in article.contents:
    if   section.name == "h2" : converter.add_header(section.contents,2)
    elif section.name == "h3" : converter.add_header(section.contents,4)

    elif section.name == "p" :
        converter.add_in_line("  \n")
        for sentence in section.contents:

            if   isinstance(sentence,str) : converter.add_in_line(sentence)
            elif sentence.name == "code"  : converter.add_code(sentence.contents)
            elif sentence.name == "b"     : converter.add_bold(sentence.contents)
            elif sentence.name == "i"     : converter.add_italic(sentence.contents)
            elif sentence.name == "a"     : converter.add_link(sentence)




with open("output.md","w",encoding="utf-8") as file:
    file.write(converter.md_str)

