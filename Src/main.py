from bs4 import BeautifulSoup
import md_converter as md_conv
import requests
import json
import sys


settings  = json.load(open("settings.json","r"))
converter = md_conv.md_converter()
converter.settings = settings


if   len(sys.argv) == 2     : to_scrape = [sys.argv[1]]
elif settings["parse list"] : to_scrape = open("to_scrape.txt","r").read().split("\n")
else                        : to_scrape = ["https://en.wikipedia.org/wiki/Markdown"]


current_article = 1
for current in to_scrape:
    

    #>>> GET VALID URL <<<#
    if   not current or current.startswith("#") : saniticed_url = ""
    elif current.startswith("https://")         : saniticed_url = current
    elif len(current.split(".")) == 3           : saniticed_url = "https://"+current
    elif len(current.split("/")) == 2           : saniticed_url = "https://"+settings["language"]+".wikipedia.org/"+current
    elif len(current.split("/")) == 1           : saniticed_url = "https://"+settings["language"]+".wikipedia.org/wiki/"+current


    #>>> PREPARATION <<<#
    if saniticed_url:
        converter.md_str = ""
        soup = BeautifulSoup(requests.get(saniticed_url).text, 'lxml')

        article = soup.find(id=settings["id of article"]).div
        title   = soup.find(id=settings["id of title"]).text

        converter.add_title(title)
        converter.add_linebreak()
        converter.add_in_line("-----------------------")


        #>>> DYNAMIC SCRAPING <<<#
        for section in article.contents:

            if   section.name == "h2" : converter.add_header(section.contents,2)
            elif section.name == "h3" : converter.add_header(section.contents,4)
            
            elif section.name == "ul" : pass
            elif section.name == "ol" : pass
            elif section.name == "tbody" or section.name == "table"     : pass
            elif section.name == "code" or section.name == "pre"  : pass

            elif section.name == "p" :
                converter.add_in_line("  \n")
                for sentence in section.contents:

                    if   isinstance(sentence,str) : converter.add_in_line(sentence)
                    elif sentence.name == "code" or sentence.name == "pre"  : converter.add_code(sentence.contents)
                    elif sentence.name == "b"     : converter.add_bold(sentence.contents)
                    elif sentence.name == "i"     : converter.add_italic(sentence.contents)
                    elif sentence.name == "a"     : converter.add_link(sentence)

            elif isinstance(section,str) or "style" in section.name or "rel" in section.name or "link" in section.name:pass      
            elif "thumb" in section.attrs["class"] and settings["media"]: converter.add_image(section.contents)


        #>>> FINISHING <<<#
        print("finished "+str(current_article)+":   "+current)
        with open("out/"+str(current_article)+".md","w",encoding="utf-8") as file:
            file.write(converter.md_str)
        current_article += 1

