import re
import scrapy
import bs4
from ..items import BookDoubanItem
class DoubanSpider(scrapy.Spider):
    name = 'book_douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']
    for x in range(10):
        url = f'https://book.douban.com/top250?start={x * 25}'
        start_urls.append(url)
    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr', class_="item")
        # 用find_all提取<tr class="item">元素，这个元素里含有书籍信息
        for data in datas:
            # 遍历data
            item = BookDoubanItem()
            # 实例化DoubanItem这个类
            item['title'] = data.find_all('a')[1]['title']
            # 提取出书名，并把这个数据放回DoubanItem类的title属性里
            item['publish'] = data.find('p', class_='pl').text
            # 提取出出版信息，并把这个数据放回DoubanItem类的publish里
            item['score'] = data.find('span', class_='rating_nums').text
            people0 = data.find('span', class_='pl').text
            pattern = re.compile("\d+")
            people1 = re.findall(pattern, people0)
            people2 = people1[0]
            item['people'] = people2
            print(item['title'])
            yield item


