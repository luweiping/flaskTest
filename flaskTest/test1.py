# -*- coding: UTF-8 -*-
#/*--------------------------------------------------------------------
# 程序名称： D:/Prog/eclipse-workspace/flashTest/test1.py
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
app = Flask('test1')

#路由和视图函数
# @app.route('/')
# def index():
#     return '<h1> Hello World!</h1>'
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

# #路由和视图函数
# @app.route('/ht')
# def htmltest():
#     return render_template("htmltest.html")

#路由和视图函数
@app.route('/ht')
def htmltest():
    return render_template("htmltest.html",str="第一个html模板+参数传递")


##路由后面如果带"/"，相当于目录，在url访问的时候，也需要带"/"结尾
##如上面的ht,若试图访问 http://127.0.0.1:5000/ht/ 则会报 Not Found

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))
 
##指定请求方法
@app.route('/login',methods=("GET","POST"))
def login():
    ##判断请求方法
    if request.method  ==  "GET":
        return render_template("login.html")
    if request.method  ==  "POST":
        print("header:"+request.headers)
        print("json:"+request.json)
        print("data:"+request.data)
         
        user_info = request.to_dict()
         
        if user_info.get("username") ==  "lwp" and user_info.get("pwd") == "123456":
            print("username:"+user_info.get("username"))
            print("pwd:"+user_info.get("pwd"))
            return  redirect("/")
 
# with  app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('profile',username='lwp'))

@app.route('/echarts')
def echarts():
    xstr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    print(xstr)
    return render_template("echarts.html",xstr="第一个html模板+参数传递")



@app.route("/weather", methods=["GET"])
def weather():
    if request.method == "GET":
        ##res = query_db("SELECT * FROM weather")
        
#     return jsonify(month=[x[0] for x in res],
#                    evaporation=[x[1] for x in res],
#                    precipitation=[x[2] for x in res])
    #"1月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"
        list_month  =   ["1月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
        list_evaporation    =   [2,4.9,7,23.2,25.6,76.7,135.6,162.2,32.6,20,6.4,3.3]
        list_precipitation  =   [2.6,5.9,9,26.4,28.7,70.7,175.6,182.2,48.7,18.8,6,2.3]
        
    return jsonify(month=["1月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"],
                   evaporation=[2,4.9,7,23.2,25.6,76.7,135.6,162.2,32.6,20,6.4,3.3],
                   precipitation=[2.6,5.9,9,26.4,28.7,70.7,175.6,182.2,48.7,18.8,6,2.3])
    

##json ajax
@app.route('/getdata')
def get_data():
    language = ['python', 'java', 'c', 'c++', 'c#', 'php']
    value = ['100', '150', '100', '90', '80', '90']
    return json.dumps({'language':language,'value':value},ensure_ascii=False) #如果有中文的话，就需要ensure_ascii=False

#启动服务器，默认ip端口为127.0.0.1:5000
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False ##jsonify中文显示异常，需要加入
    app.run(debug=True)
   
    