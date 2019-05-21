from HelloAMGO.app.dbModule import *

class dbConnection:
    def __init__(self, sql):
        self.sql = sql

    def tryConnect(self):
        db1 = Database()

        try:
            with db1.cursor() as cursor:
                sql = self.sql
                cursor.execute(sql)
                db1.commit()
        finally:
            db1.close()


