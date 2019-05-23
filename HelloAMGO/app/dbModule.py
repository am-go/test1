import pymysql


class Database():
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'AMGO',
                db = 'AMGO',
                charset = 'utf8'
            )
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            print("DBerror가 발생헀습니다!!", e)
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()


