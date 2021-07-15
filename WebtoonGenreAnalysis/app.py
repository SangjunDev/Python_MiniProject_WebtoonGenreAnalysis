#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import cx_Oracle
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

cx_Oracle.init_oracle_client(config_dir=r"C:\dev\OracleWallet\Wallet_andongdb")
connect = cx_Oracle.connect(user="team4", password='andongProjectUser4', dsn='andongdb_high')
cur = connect.cursor()

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index.html/')
def index_1():
	return render_template('index.html')

@app.route('/platform.html')
def platform():

	aa=pd.read_sql("select * from addweb where platform='네이버 웹툰' and genre2=' 로맨스'", con = connect)
	firsttitle=aa.loc[0][1]
	secondtitle=aa.loc[1][1]
	thirdtitle=aa.loc[2][1]

	bb=pd.read_sql("select * from addweb where platform='다음 웹툰' AND (genre1='순정' OR genre2=' 로맨스')", con = connect)
	firsttitle2=bb.loc[0][1]
	secondtitle2=bb.loc[1][1]
	thirdtitle2=bb.loc[2][1]

	cc=pd.read_sql("select * from addweb where platform='카카오' AND genre1='소년'", con = connect)
	firsttitle3=cc.loc[0][1]
	secondtitle3=cc.loc[1][1]
	thirdtitle3=cc.loc[2][1]

	dd=pd.read_sql("select * from addweb where platform='레진코믹스 웹툰' AND (genre1='로맨스' OR genre1='BL' OR genre1='백합')", con = connect)
	firsttitle4=dd.loc[0][1]
	secondtitle4=dd.loc[1][1]
	thirdtitle4=dd.loc[2][1]

	return render_template('platform.html',firsttitle=firsttitle, secondtitle=secondtitle, thirdtitle=thirdtitle,
	firsttitle2=firsttitle2, secondtitle2=secondtitle2, thirdtitle2=thirdtitle2,
	firsttitle3=firsttitle3, secondtitle3=secondtitle3, thirdtitle3=thirdtitle3,
	firsttitle4=firsttitle4, secondtitle4=secondtitle4, thirdtitle4=thirdtitle4)



	return render_template('platform.html')

@app.route('/genre.html')
def genre():
	return render_template('genre.html')

@app.route('/day.html')
def day():
	return render_template('day.html')


@app.route('/action.html')
def action():
	return render_template('action.html')

@app.route('/daily.html')
def daily():
	return render_template('daily.html')

@app.route('/etc.html')
def etc():
	return render_template('etc.html')

@app.route('/fantagy.html')
def fantagy():
	return render_template('fantagy.html')

@app.route('/Fri.html')
def Fri():

	fr=pd.read_sql("select * from addweb where day='금'", con = connect)
	frlist=[]
	for i in range(50):
		frlist.append(fr.loc[i][1])

	return render_template('Fri.html',frlist=frlist)

@app.route('/mon.html')
def mon():
	m=pd.read_sql("select * from addweb where day='월'", con = connect)
	mmlist=[]
	for i in range(50):
		mmlist.append(m.loc[i][1])

	return render_template('mon.html',mmlist=mmlist)

@app.route('/mystery.html')
def mystery():
	return render_template('mystery.html')

@app.route('/romance.html')
def romance():
	return render_template('romance.html')

@app.route('/sat.html')
def sat():

	sa=pd.read_sql("select * from addweb where day='토'", con = connect)
	salist=[]
	for i in range(50):
		salist.append(sa.loc[i][1])


	return render_template('sat.html',salist=salist)

@app.route('/sport.html')
def sport():
	return render_template('sport.html')

@app.route('/sun.html')
def sun():

	su=pd.read_sql("select * from addweb where day='일'", con = connect)
	sulist=[]
	for i in range(50):
		sulist.append(su.loc[i][1])

	return render_template('sun.html',sulist=sulist)

@app.route('/thu.html')
def thu():

	th=pd.read_sql("select * from addweb where day='목'", con = connect)
	thlist=[]
	for i in range(50):
		thlist.append(th.loc[i][1])

	return render_template('thu.html',thlist=thlist)

@app.route('/tue.html')
def tue():

	t=pd.read_sql("select * from addweb where day='화'", con = connect)
	ttlist=[]
	for i in range(50):
		ttlist.append(t.loc[i][1])


	return render_template('tue.html',ttlist=ttlist)

@app.route('/wed.html')
def wed():

	w=pd.read_sql("select * from addweb where day='수'", con = connect)
	wwlist=[]
	for i in range(50):
		wwlist.append(w.loc[i][1])

	return render_template('wed.html',wwlist=wwlist)

@app.route('/post', methods=['GET','POST'])
def post():
	value = request.form['webtoon_name']
	a=pd.read_sql("select * from addweb where title='"+value+"'", con = connect)
	author = a.loc[0][2] #작가
	day=a.loc[0][3] #날짜
	genre=a.loc[0][4] #장르
	story=a.loc[0][6] #스토리
	img=a.loc[0][8] # 이미지 경로
	return render_template('search.html',author = author, day=day,genre=genre,story=story,img=img)



@app.route('/naver.html')
def naver():
	n=pd.read_sql("select * from addweb where platform='네이버 웹툰'", con = connect)
	nnlist=[]
	for i in range(50):
		nnlist.append(n.loc[i][1])
	return render_template('naver.html',nnlist=nnlist)


@app.route('/daum.html')
def daum():
	d=pd.read_sql("select * from addweb where platform='다음 웹툰'", con = connect)
	ddlist=[]
	for i in range(50):
		ddlist.append(d.loc[i][1])
	return render_template('daum.html',ddlist=ddlist)

@app.route('/kakaopage.html')
def kakaopage():
	k=pd.read_sql("select * from addweb where platform='카카오'", con = connect)
	kklist=[]
	for i in range(50):
		kklist.append(k.loc[i][1])
	return render_template('kakaopage.html',kklist=kklist)


@app.route('/lezhin.html')
def lezhin():
	r=pd.read_sql("select * from addweb where platform='레진코믹스 웹툰'", con = connect)
	rrlist=[]
	for i in range(50):
		rrlist.append(r.loc[i][1])
	return render_template('lezhin.html',rrlist=rrlist)





if __name__ == '__main__':
	app.run( debug=True)
