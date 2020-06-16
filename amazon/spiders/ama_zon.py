# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem
      

class AmaZonSpider(scrapy.Spider):
    name = 'fiver'
    page_number = 2  #you can start fro page_number = 0
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1591558402&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        
        items = AmazonItem()

        author=[]

        title = response.css(".a-color-base.a-text-normal").css("::text").extract()
        
        for value in response.css(".sg-col-12-of-28 span.a-size-base+ .a-size-base::text").getall():
            author.append(" ".join(value.split()))
      
        
        price = response.css(".a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole").css("::text").extract()
        image_link = response.css(".s-image::attr(srcset)").extract()
        books = print(author,title,price,image_link)
        
        items["Title"] = title
        items["Author"] = author
        items["Price"] = price
        items["image_link"] = image_link
      

        yield items 

        next_page = "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page="+ str (AmaZonSpider.page_number) + "&fst=as%3Aoff&qid=1591562327&rnid=1250225011&ref=sr_pg_2"
        
        if AmaZonSpider.page_number <= 18:
            AmaZonSpider.page_number +=1
        
            yield response.follow(next_page , callback = self.parse)
