from flask import *
import sqlite3
import datetime
import time
import pyautogui as pg
import win32com.client
import pythoncom

hostname = ""
hostclassname = ""
hostpassword = ""

dt_now = datetime.datetime.now()
week_list = ['月', '火', '水', '木', '金', '土', '日']

year_now = dt_now.year
month_now = dt_now.month
day_now = dt_now.day

dt = datetime.datetime(year_now,month_now,day_now)
week = week_list[dt.weekday()]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


###############################################################
#####           氏名と学籍番号によるログイン処理             #####
###############################################################

@app.route('/home', methods=['POST'])
def login():

    #index.htmlで入力された'名前'と'学籍番号'を取得
    loginname = request.form.get('loginname')
    loginpassword = request.form.get('loginpassword')

    #データベースを新規作成 or 読み込み nkc=名古屋工学院専門学校
    databasename = 'nkc.db'
    db = sqlite3.connect(databasename)
    cur = db.cursor()
    
    #入力された学籍番号の生徒の名前を取得
    cur.execute('select * from student_table where STUDENT_NUMBER = ?', (loginpassword,))
    student_info = cur.fetchone()
    cur.close()
    db.close()
    
    #学籍番号がなく、データの取得が出来なかった場合
    if not student_info:
        return render_template('index.html')
    #データを取得した場合、STUDENT_NAME列（名前）CLASS_NAME（クラス名）のデータを取得
    else:
        studentclassname = student_info[1]
        studentname = student_info[2]

    #ログイン名とデータベースで取得した名前が一致しているか
    if loginname == studentname :
        global hostname
        hostname = studentname
        global hostclassname
        hostclassname = studentclassname
        global hostpassword
        hostpassword = loginpassword

        return render_template('home.html', hostname=hostname, hostclassname=hostclassname)
    else:
        return render_template('index.html')
    

#################################################
#####           各項目クリック処理           #####
#################################################

#＞＞ 日誌がクリックされた場合
@app.route('/diary', methods=['POST'])
def select_diary():
    return render_template('diary.html', year_now = year_now, month_now = month_now, day_now = day_now, week = week, hostname = hostname)

#＞＞ 欠席・欠課・遅刻　届がクリックされた場合
@app.route('/absence', methods=['POST'])
def select_absence():
    return render_template('absence.html', year_now = year_now, month_now = month_now, day_now = day_now, week = week, hostname = hostname, hostpassword = hostpassword, hostclassname=hostclassname)

#＞＞ 公欠願書
@app.route('/authorized_absence', methods=['POST'])
def select_authorized_absence():
    return render_template('authorized_absence.html', year_now = year_now, month_now = month_now, day_now = day_now, week = week, hostname = hostname, hostclassname=hostclassname)


#################################################
#####           書類自動提出処理             #####
#################################################

@app.route('/submit/<roll>', methods=['POST'])
def submit(roll):
    #入力ページをpdfでダウンロードする
    pg.press('alt')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('p')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('enter')
    time.sleep(4)

    #ダウンロードしたpdfをメールで送信する
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch('Outlook.Application')
    mymail = outlook.CreateItem(0)

    mymail.BodyFormat = 3
    mymail.To = 'test.mai1desu0@gmail.com'
    if roll == 'diary':
        mymail.Subject = '日誌提出'
        mymail.Body = '本日の日誌です。確認お願いします。'
        mymail.Attachments.Add ('C:\\Users\\user\\Downloads\\日誌.pdf')
    elif roll == 'absence':
        mymail.Subject = '欠席・欠課・遅刻提出'
        mymail.Body = '欠席・欠課・遅刻　届です。確認お願いします。'
        mymail.Attachments.Add ('C:\\Users\\user\\Downloads\\欠席・欠課・遅刻.pdf')
    elif roll == 'authorized_absence':
        mymail.Subject = '公欠願書提出'
        mymail.Body = '公欠願書です。確認お願いします。'
        mymail.Attachments.Add ('C:\\Users\\user\\Downloads\\公欠願書.pdf')
    
    mymail.Send()

    time.sleep(3)

    return render_template('home.html', hostname=hostname, hostclassname=hostclassname)


#################################################
#####           サーバー接続処理             #####
#################################################

def main():
    app.debug = True
    app.run(host = 'localhost', port = 8080)

if __name__ == '__main__':
    main()