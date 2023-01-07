![Mark down Wikipedia](banner.png)

<h3 align="center">Scrape Wikipedia into .md-files</h3>
<p align="center">
    <a href="#Installation">Installation</a> •
    <a href="#Usage">Usage</a> •
    <a href="#WIP">WIP</a> •
    <a href="#License">License</a>
</p>

---

## Description  

This script takes your given url to an Wikipedia-entry and converts it into a md-file.
  
It can be usefull on itself to extract the relevant content of the webpage into a **more compatible and readable format**.  
In bigger project, it can be used as a **Subsystem for automation or Webscrapping**.  
  
---
  
## Installation  
  
The only prerequisite is [**Python**](https://www.python.org/downloads/).

```bash
git clone https://github.com/Daniel-RRR/MarkDownWikipedia.git
```
  
---
  
## Usage
  
### Enter url as parameter
````bash
python main.py https://en.wikipedia.org/wiki/Markdown
````  
  
Can be shortend to the **name** of article, will be written in **language of settings**.
````bash
python main.py markdown            
````  
  
Shortend urls can use a **specific languages** by adding ``lang=`` and its **abbreviation** as second argument
````bash
python main.py markdown lang=pl    # polish             
````  
  
further valid formats:
````bash
python main.py en.wikipedia.org/wiki/Markdown  
python main.py wiki/Markdown
````

### Itterate through to_scrape.txt
content is split by ``\n``  
write comments by ``#``  
empty lines are valid    
  
all of the following formats are valid
````bash
https://en.wikipedia.org/wiki/Markdown

# multi-langugage support
es.wikipedia.org/wiki/Markdown
pl.wikipedia.org/wiki/Markdown

# back to your default set in settings.json
wiki/markdown
markdown

# lang for specific 
markdown lang=pl
````
  
#### configurables in settings.json
| key                 | description                          | default            |
|---------------------|--------------------------------------|--------------------|
| id of article       | id of article for BeautyfulSoup      | mw-content-text    |
| id of title         | id of title for BeautyfulSoup        | firstHeading       |
| parse list          | parse list.txt of urls               | false              |
| plaintext           | no markdown, just ascii              | false              |
| media               | pictures and references to videos    | true               |
| language            | domain of wikipedia to reference     | en                 |
| meta-data            | adds header with meta info          | true               |
  
---
  
## WIP
  
* table, code/pre, ul/ol
* generate TOC
* write down meta-data of generation
* plaintext

  
---
  
## License

This project is licensed under the terms of the
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0).  
  
  
  