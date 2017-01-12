# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.request import Request
import requests



class LolkingspiderSpider(scrapy.Spider):
    name = "lolkingspider"
    allowed_domains = ["lolking.net"]
    payload = 'region=na&type=champion-winrate&range=weekly&map=sr&queue=1x1'
    start_urls = (
        'http://www.lolking.net/charts?%s' %payload,
    )
    headers = {"Host": "m.ctrip.com",
            "User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            "cookieOrigin": "http://wap.ctrip.com",
            "Cache-Control": "no-cache",
            "Referer": "http://wap.ctrip.com/webapp/hotel/hoteldetail/426638.html?days=1&atime=20160623&contrl=2&num=1&biz=1",
            "Content-Length": "455",
            "Origin": "http://wap.ctrip.com",
            "Connection": "keep-alive"}

    def parse(self, response):
        """for item in response.css(''):"""
        self.logger.info(response.url)
        print(response.css('span.header-champion-name strong::text').extract())
        a=response.body
        a=a.decode("utf-8")
        c=re.findall(r'name............(.*?)\\',a)
        print(c)
        i2 = 0
        for i in c:
            if (i2<20 and i2>9):
                print (i)
            i2 +=1
        #c=response.xpath('//script')
        #for i in c:
        #    print (i)
        #print(c)

        #b=a.decode('utf-8')
        #b=re.findall(r'name............(.*?)\\', a)
        #print (b)
        filename = 'lolking.html'
        with open(filename,'wb')as f:
            f.write(response.body)
        self.log("Saved")

