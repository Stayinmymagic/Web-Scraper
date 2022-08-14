
import scrapy
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import time
import random

#%%
topics = ['aerospace']
topics = ['us', 'europe', 'china', 'asia', 'uk', 'middle east']#All done
topics = ['fed', 'currencies', 'commodity', 'retail', 'consumer', 'politics',
          'finance', 'media', 'telecom', 'autos', 'transportation',
          'sustainable', 'technology', 'energy', 'environment','defense']
topics = ['finance']
topics = ['United States']
#%%
class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    #allowed_domains = ['www.forbes.com']
    
    def start_requests(self):
        for topic in topics:
            url = 'https://www.forbes.com/simple-data/search/?sort=relavant&q=%s&sh=18f97ab6279f'%topic
            yield scrapy.Request(url = url, callback=self.parse, meta = {'topic' : topic})

    def parse(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        pages = int(soup.find('div').get('count'))//20
        links = soup.select('.stream-item__title')
        
        description = soup.select('.stream-item__description')
        for i in range(len(links)):
            #print(re.search(r'[0-9]+/[0-9]+/[0-9]+', links[i*2].get('href')).group(0))
            ReutersItem = {
                'link' : links[i].get('href'),
                'date' : re.search(r'[0-9]{4}/[0-9]{2}/[0-9]{2}', links[i].get('href')).group(0),
                'title': links[i].text,
                'topic': response.meta['topic'],
                'summary': re.sub('[^A-Za-z0-9,.]+',' ', description[i].text),
            }
            yield ReutersItem
            

        for page in range(1, pages+1):
            print('page : ', page)
            url = 'https://www.forbes.com/simple-data/search/more/?start=%i&sort=relevant&q=%s&sh=18f97ab6279f'%(page*20,response.meta['topic'])
            yield scrapy.Request(url = url, callback=self.save2db, meta = {'topic' : response.meta['topic']})
            time.sleep(random.randint(1,3))
        #title = response.xpath('//*[@id="content"]/section[2]/div/div[1]/div[4]/div/div[3]/div[2]/div/h3/a').extract()
        #time = response.xpath('//*[@id="content"]/section[2]/div/div[1]/div[4]/div/div[3]/div[2]/div/h5').extract()
        #item = {'title':title,
        #        'time':time}
        
        #print(response.request.headers)'''
        #yield {'text':response.text}
    def save2db(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        links = soup.select('.stream-item__title')
        description = soup.select('.stream-item__description')
        for i in range(len(links)):
            #print(re.search(r'[0-9]+/[0-9]+/[0-9]+', links[i*2].get('href')).group(0))
            ReutersItem = {
                'link' : links[i].get('href'),
                'date' : re.search(r'[0-9]{4}/[0-9]{2}/[0-9]{2}', links[i].get('href')).group(0),
                'title': links[i].text,
                'topic': response.meta['topic'],
                'summary': re.sub('[^A-Za-z0-9,.]+',' ', description[i].text),
            }
            
            yield ReutersItem
        
#%%
'''
class ReutersSpider(scrapy.Spider):
    name = 'reuters_for_old'
    #allowed_domains = ['www.forbes.com']
    
    def start_requests(self):
        for topic in topics:
            url = 'https://www.forbes.com/simple-data/search/?sort=relavant&q=%s&sh=18f97ab6279f'%topic
            yield scrapy.Request(url = url, callback=self.parse, meta = {'topic' : topic})

    def parse(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        pages = int(soup.find('div').get('count'))//20
        links = soup.select('.stream-item__title')
        
        description = soup.select('.stream-item__description')
        
        for i in range(len(links)):
            #print(re.search(r'[0-9]+/[0-9]+/[0-9]+', links[i*2].get('href')).group(0))
            ReutersItem = {
                'link' : links[i].get('href'),
                'date' : re.search(r'[0-9]{4}/[0-9]{2}/[0-9]{2}', links[i].get('href')).group(0),
                'title': links[i].text,
                'topic': response.meta['topic'],
                'summary': re.sub('[^A-Za-z0-9,.]+',' ', description[i].text),
            }
            yield ReutersItem
      

        for page in range(9863, pages+1):
            print('page : ', page)
            url = 'https://www.forbes.com/simple-data/search/more/?start=%i&sort=relevant&q=%s&sh=18f97ab6279f'%(page*20,response.meta['topic'])
            yield scrapy.Request(url = url, callback=self.save2db, meta = {'topic' : response.meta['topic']})
            time.sleep(random.randint(1,3))
        #title = response.xpath('//*[@id="content"]/section[2]/div/div[1]/div[4]/div/div[3]/div[2]/div/h3/a').extract()
        #time = response.xpath('//*[@id="content"]/section[2]/div/div[1]/div[4]/div/div[3]/div[2]/div/h5').extract()
        #item = {'title':title,
        #        'time':time}
        
        #print(response.request.headers)
        #yield {'text':response.text}
    def save2db(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        links = soup.select('.stream-item__title')
        description = soup.select('.stream-item__description')
        for i in range(len(links)):
            #print(re.search(r'[0-9]+/[0-9]+/[0-9]+', links[i*2].get('href')).group(0))
            ReutersItem = {
                'link' : links[i].get('href'),
                'date' : re.search(r'[0-9]{4}/[0-9]{2}/[0-9]{2}', links[i].get('href')).group(0),
                'title': links[i].text,
                'topic': response.meta['topic'],
                'summary': re.sub('[^A-Za-z0-9,.]+',' ', description[i].text),
            }
            
            yield ReutersItem     
#%%       
class ProxyExampleSpider(scrapy.Spider):
    name = "test"
    # start_urls = ['https://httpbin.org/ip']
    def start_requests(self):
        for i in range(5):
            yield scrapy.Request('https://httpbin.org/ip', dont_filter=True)

    def parse(self, response):
        print(response.text)
        print(response.request.headers)

#%%%


'''
