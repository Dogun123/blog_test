from flask import Flask
from blueprint import blog_test


app = Flask(__name__)
app.register_blueprint(blog_test.blog_ab,url_prefix='/blog')

if __name__ == '__main__':
    app.run(host='localhost',port='8080')