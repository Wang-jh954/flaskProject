# 导入 Flask 对象
from flask import Flask,render_template

# 使用Flask对象创建一个app对象
app = Flask(__name__)


# 路由
@app.route('/')  # “/” 访问的路径  “@” 生成器
def hello_world():  # put application's code here
    return 'HBNU'


@app.route('/login')
def login():
    # 登录的功能
    return render_template('login.html')


# 实现其他功能怎么做(例如退出、查看学生信息）等等的其他功能、该怎么实现
# @app.route('/login_out')


if __name__ == '__main__':
    app.run()
