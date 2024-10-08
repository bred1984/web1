import psycopg2
from psycopg2.extras import RealDictCursor
from sql_db import *



class SqlDriver:
    con:None
    cur:None
    data:None
    # def __init__(self):
    #     SqlDriver.con = psycopg2.connect(host='localhost',
    #                                user='postgres',
    #                                password='123321',
    #                                dbname="socnetwork",
    #                                port="5432")
        # self.con=con

    @staticmethod
    def connect(f,data=0):
        # self.data=data
        SqlDriver.con = psycopg2.connect(host='localhost',
                                         user='postgres',
                                         password='123321',
                                         dbname="socnetwork",
                                         port="5432")
        SqlDriver.data=data
        with SqlDriver.con:
            # создаем объект для запуска sql запросов
            SqlDriver.cur = SqlDriver.con.cursor(cursor_factory=RealDictCursor)
            # self.cur=cur
            f()
            SqlDriver.cur.close()
        print('curclose')

    @staticmethod
    def insert_db():
        db={'name': 'users', 'sql': "insert into users (fio, age, pasport) values('Иванов',31,'qwertytuy')"}
        sql=f"insert into users (fio, age, pasport) values('{SqlDriver.data['fio']}',{SqlDriver.data['age']},'{SqlDriver.data['pasport']}')"
        # self.con()
        SqlDriver.cur.execute(sql)
        # self.cur.close()

    def CreateDB(self):
        for s in sql_create_table:
            SqlDriver.cur.execute(s['sql'])

