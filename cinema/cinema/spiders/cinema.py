#!/usr/bin/env python
# coding: utf-8

# In[5]:


import scrapy


class cinema(scrapy.Spider):
    name = "cinema"
    start_urls = [
        'https://transcripts.fandom.com/wiki/Avengers:_Endgame',
    ]

    def parse(self, response):
        rawtext=response.xpath(".//div[@class='mw-content-ltr mw-content-text']//p").extract()
        for raw in rawtext:
            yield{
                    'name':raw
                    }
      



# In[ ]:




