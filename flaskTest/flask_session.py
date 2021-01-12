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
# 1 、要求:
#     1.登录页面
#     2.学生概况页面 ID name 点击详情
#     3.学生详情页面 ID name age gender

# 2.使用session验证登录状态
# 思考:如何记录登录次数

# 3.基于Session编写登录验证装饰器
# 思考:如何给两个以上的视图函数增加装饰器
#初始化
from flask import Flask, request, redirect, render_template, session
from functools import wraps

USER = {'username': 'anwen', 'password': "123"}
STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}
app = Flask(__name__)
app.secret_key = "!@#$%^&*()"
app.debug = True

# 装饰器装饰多个视图函数
def wrapper(func):
    @wraps(func)  # 保存原来函数的所有属性,包括文件名
    def inner(*args, **kwargs):
        # 校验session
        if session.get("user"):
            ret = func(*args, **kwargs)  # func = home
            return ret
        else:
            return redirect("/login")
    return inner


# 首页
@app.route('/')
@wrapper
def index():
    # if session.get('user'):
    return render_template('index.html')
    # else:
    #     return redirect("/login")


# 登录
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.form.get("username") == USER["username"] and request.form.get("password") == USER["password"]:
            session["user"] = request.form.get("username")
            return redirect("/")
        else:
            return redirect("/login")


# 学生概况页面
@app.route('/desc')
@wrapper
def desc():
    # if session.get("user"):
    return render_template('desc.html', stu_dic=STUDENT_DICT)
    # else:
    #     return redirect("/login")


# 学生详情页面
@app.route('/info')
@wrapper
def info():
    # if session.get("user"):
    return render_template('info.html', stu_dic=STUDENT_DICT)
    # else:
    #     return redirect("/login")

#启动服务器，默认ip端口为127.0.0.1:5000
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False ##jsonify中文显示异常，需要加入
    app.run(debug=True)
   
    