# -*- coding: utf-8 -*-
import scrapy


class BabastudioSpider(scrapy.Spider):
    name = 'babastudio'
    # ini halaman yang akan di scraping
    start_urls = ['https://academy.babastudio.com/course-package-frontend']

    def parse(self, response):
        #ini mengambil data dengan tag div yang class nya course__box
        all_kursus = response.css('div.course__box')
        for kursus in all_kursus:
            #ini mengambil nama kursus,price,image
            title = kursus.css('p.title::text').extract()
            price = kursus.css('strong::text').extract()
            image = kursus.css('img.img-responsive').attrib['src']
            #ini menyatukan beberapa data ketika akan ditampilkan membentuk suatu ksatuan
            yield{
                'title' : title,
                'price' : price,
                'image' : image
            }
