![Mark down Wikipedia](banner.png)

<h3 align="center">Scrape Wikipedia Articles into .md-files</h3>
<p align="center">
    <a href="#Installation">Installation</a> •
    <a href="#Usage">Usage</a> •
    <a href="#WIP">WIP</a> •
    <a href="#Bugs">Bugs</a> •
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
  
###### enter url as parameter
````bash
python Src/main.py https://"+settings["language"]+".org/wiki/Markdown
````
  
###### configurable options
| key                 | description                          | default            |
|---------------------|--------------------------------------|--------------------|
| default output      | filepath of finished scrape          | output.md          |
| id of article       | id of article for BeautyfulSoup      | mw-content-text    |
| id of title         | id of title for BeautyfulSoup        | mw-page-title-main |
| parse list          | parse list.txt of urls               | false              |
| plaintext           | no markdown, just ascii              | false              |
| media               | pictures and references to videos    | true               |
| language            | domain of wikipedia to reference     | en                 |
| meta-data            | adds header with meta info     | true                 |
  
---
  
## WIP
  
* MVP (table,code,ul,ol,img)
* generate TOC
* actual implementation of settings.json (currently stub only)
* write down meta-data of generation
* use ``-a`` parameter to convert a list of url saved in a file
* use ``-r`` parameter to convert in plain-text, without md-keywords
* use ``-m`` parameter to convert also the pictures of an article
* use ``-u`` parameter followed by the url to set the article by a cli arg

---

## Bugs

* links refering to wikipedia needs to be in the same language as set in settings (i.e. **en** for ``"+settings["language"]+".org`` )
  
---
  
## License

This project is licensed under the terms of the
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0).  
  
  
  