from HelloAMGO import application
from flask import g, json, make_response, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *
import pymysql

test_univ = '한국외대'
test_year =  '2018'
test_num ='1-1'


@application.route("/board/confirm", methods=['POST'])
def testUniv():
    global test_univ
    test_univ = request.form.get('test_univ')
    return redirect(url_for('board_list'))

@application.route("/board-list/confirm", methods=['POST'])
def testList():
    global test_year
    global test_num
    test_year = request.form['options_y']
    test_num = request.form['options_x']
    return redirect(url_for('board_answer'))

@application.route("/board-answer/confirm", methods=['POST'])
def testAnswer():
    global test_title
    global test_content
    test_title = request.form.get('title')
    test_content = request.form.get('content')

    try:
        conn = Database()
        i=1

        sql = "INSERT INTO test(index, univ, year, num, title, contents) VALUES(\"%s\",\"%s\",\"%s\", \"%s\", \"%s\", \"%s\")" % (i,test_univ,test_year,test_num, test_title, test_content);
        print(sql)
        conn.execute(sql)
        conn.commit()
        return redirect(url_for('index_load'))
    except Exception as ex:  # 에러 종류
        print('에러가 발생 했습니다', ex)
        return redirect(url_for('login'))