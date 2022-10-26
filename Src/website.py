from urllib.parse import urlparse
from urllib import request


class Website:


  def set_url(self, url:str):
    if url.startswith("https://") is False:
      url = "https://" + url

    if url.__contains__("wikipedia.org") is False:
      raise Exception("\"wikipedia.org\" not recogniced in given URL! please check its validity")
    
    if urlparse(url) is False: 
      raise Exception("Wikipedia entry not found!")

    print("url set successfull!")
    self._url = url
  

  def download_source(self):
    with request.urlopen(self._url) as req: 
      self._raw_html = req.read().decode('utf-8')


  def extract_article(self, begin_id:str, end_id:str):
    if self._raw_html.__contains__(begin_id) is False:
      raise Exception(begin_id+"is not found in source!")
    if self._raw_html.__contains__(end_id) is False:
      raise Exception(end_id+"is not found in source!")

    article_begin = self._raw_html.split(begin_id)[1]
    self._raw_article = article_begin.split(end_id)[0]
    
    