# -*- coding: UTF-8 -*-
#/*--------------------------------------------------------------------
# 程序名称： D:/Prog/eclipse-workspace/flashTest/test2.py
# 执行环境： python3.x
# 程序描述： 获取基金重仓持股信息
# 输入参数： 
#         
# 输出参数： 无
# 涉及实体： 
# 产生实体： 
# 编写人员：3468
# 创建日期：2020年12月18日
# 修改日期：
# 修改内容：
# 代码版本：
# 公司名称：lwp 
#----------------------------------------------------------------------*/

#初始化
from flask import Flask,render_template,url_for,escape,request,redirect,jsonify,json
from flask.helpers import url_for
# app = Flask(__name__)
app = Flask('app')

#路由和视图函数
# @app.route('/')
# def index():
#     return '<h1> Hello World!</h1>'
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


##调用路由，返回的是个数据，如果直接在url中访问/weather，显示的是json数据，需要在js中调用url获取数据
@app.route("/weather", methods=["GET","POST"])
def weather():
    if request.method == "POST" or request.method == "GET" :
        list_month  =   ["1月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
        list_evaporation    =   [2,4.9,7,23.2,25.6,76.7,135.6,162.2,32.6,20,6.4,3.3]
        list_precipitation  =   [2.6,5.9,9,26.4,28.7,70.7,175.6,182.2,48.7,18.8,6,2.3]
        
        return jsonify(month=list_month,
                   evaporation=list_evaporation,
                   precipitation=list_precipitation
                   )
        
@app.route('/map')
def map():
    return render_template('map.html')     

#启动服务器，默认ip端口为127.0.0.1:5000
if  __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False ##jsonify中文显示异常，需要加入
    app.run(debug=True)
   
    