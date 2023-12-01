# 导入 Flask 对象
from flask import Flask

# 使用Flask对象创建一个app对象
app = Flask(__name__)


# 路由
@app.route('/')  # “/” 访问的路径  “@” 生成器
def hello_world():  # put application's code here
    return 'HBNU'


@app.route('/login')
def login():
    # 登录的功能
    return '需要实现登录的逻辑'


if __name__ == '__main__':
    app.run()
