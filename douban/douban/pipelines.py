from itemadapter import ItemAdapter
import pymysql
# 连接数据库
def dbHandle():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="123456",
        charset="utf8",
        use_unicode=False
    )
    return conn
class HellospiderPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE scrapy_songs")
        # 插入数据库
        sql = "INSERT INTO book(title,publish,score,people) VALUES(%s,%s,%s,%s)"
        try:
            cursor.execute(sql,
                           (item['title'], item['publish'], item['score'], item['people']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item
