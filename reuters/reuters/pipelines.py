# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from reuters import settings
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ReutersPipeline:
    def __init__(self):
 
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USERNAME,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8'
        )
 
        self.cursor = self.connect.cursor()
        
    def process_item(self, item, spider):
    
        sql_insert = 'INSERT INTO forbes (link, date, title, topic, summary)VALUES(%s,%s,%s,%s,%s)'
        data = (item['link'], item['date'],  item['title'],  item['topic'],  item['summary'])
        self.connect.ping(reconnect = True)
        self.cursor.execute(sql_insert, data)
        self.connect.commit()
        return item
    def close_spider(self, spider):
        
        self.connect.close()

