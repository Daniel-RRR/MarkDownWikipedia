from bs4 import BeautifulSoup
from soupsieve import bs4

class md_converter:
    md_str = ""
    current_declared_collumns = []
    language =""



    def _sanitice_str(self,content,keyword="SENTENCE") -> str:
        if "SENTENCE" in keyword : 
            if   isinstance(content[0],bs4.Tag) : keyword = "INNER_TAG"
            elif isinstance(content,list)       : return content[0]
            elif isinstance(content,str)        : return content 

        if "HEADER" in keyword : 
            if   len(content) == 2              : return content[0].contents[0]
            elif len(content) == 3              : return content[1].contents[0]

        if "INNER_TAG" in keyword : 
            if len(content[0].contents) != 0:content_str = content[0].contents[0]
            else: return content[1].text
            if content[0].name == "b"           : return "**"+content_str+"**"
            if content[0].name == "i"           : return "*"+content_str+"*"
            if content[0].name == "a"           : return "["+content_str+"]("+content[0].attrs["href"]+")" if content[0].attrs["href"].startswith("http") else "["+content_str+"]("+"https://"+self.language+".wikipedia.org"+content[0].attrs["href"]+")"
            #if content[0].name == "link"        : content[0].parent.attrs["href"]#return "["+content_str+"]("+content[0].parent.attrs["href"]+")"

    def _append_md_str(self,content) -> str:    
        self.md_str += content



    #>>> BASIC <<<#
    def add_line(self,content) -> None:
        content = self._sanitice_str(content)
        self._append_md_str(content+"\n")

    def add_in_line(self,content) -> None:
        content = self._sanitice_str(content)
        self._append_md_str(content)

    def add_linebreak(self,lines=1) -> None:
        self._append_md_str("\n"*lines)


    #>>> APPEARENCE <<<#
    def add_bold(self,content) -> None:
        content = self._sanitice_str(content)
        self._append_md_str( "**"+content+"**")

    def add_italic(self,content) -> None:
        content = self._sanitice_str(content)
        self._append_md_str("*"+content+"*")
    
    def add_image(self,content) -> None:
        media = content[0].contents[0]
        #self._append_md_str("----\n  ")        
        self.add_linebreak()
        if "video" in media.name:
            url = "https://"+self.language+".wikipedia.org"+content[0].contents[2].contents[0].contents[0].attrs["href"]
            self.add_bold("![VIDEO:"+content[0].contents[2].contents[1]+"]("+url+")")
        elif "a" in media.name:
            img = media.contents[0]
            self._append_md_str("!["+img.attrs["alt"]+"](https:"+img.attrs["src"]+")  \n")
            self.add_italic(""+content[0].contents[2].contents[1].strip())
        self.add_linebreak()
        #self._append_md_str("  \n----\n  ")        

    #>>> STRUCTURE <<<#
    def add_link(self,content,size=3) -> None: 
        link = content.attrs["href"]
        saniticed_link = link if link.startswith("http") else "https://"+self.language+".wikipedia.org"+link
        saniticed_text = self._sanitice_str(content.contents)
        self.md_str += "["+saniticed_text+"]("+saniticed_link+")"

    def add_code(self,content,size=3) -> None: pass

    def add_title(self,content,size=3) -> None:
        content = self._sanitice_str(content)
        self._append_md_str("#"*size+" "+content+"\n")

    def add_header(self,content,size=3) -> None:
        if size < 3 : self.add_line("\n\n -----------------------")
        content = self._sanitice_str(content,"HEADER")
        self._append_md_str("  \n  \n"+"#"*size+" "+content+"\n")



    #>>> TABLE <<<#
    def finish_table(self,collumns:list) -> None:
        self.current_declared_collumns = []
        self.md_str += "\n"

    def declare_table(self,collumns:list) -> None:
        self.current_declared_collumns = collumns
        separator = []
        for _ in range(len(collumns)):  separator.append(" -- ")
        self.append_table(collumns)
        self.append_table(separator)

    def append_table(self,collumns:list) -> None:
        if len(self.current_declared_collumns) != len(collumns):
            print("ERROR:"+str(self.current_declared_collumns)+"expected but found "+str(len(collumns))+"!  ("+str(collumns)+")")
            return None
        for entry in collumns:
            self.md_str +=self._append_md_str(str("| ")+str(entry)+" ",False) #cachedStr +=str("| ")+str(entry)+" "
        self.md_str += self._append_md_str("| \n",False)#cachedStr += str("| \n")
            





