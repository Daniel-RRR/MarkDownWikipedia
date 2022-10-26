from website import Website


url = "enter the url of an article"

next_up_id = "mw-navigation"
article_id = "mw-content-text"


website_request = Website()

website_request.set_url(url)
website_request.download_source()
website_request.extract_article(article_id,next_up_id)

print(website_request._raw_article)







