from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from app.models.core import db
from app.models.model import User
from app.api.api import bp
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(os.path.dirname(__name__),'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/flaskdemo2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(bp)
db.app = app
db.init_app(app)




@app.route('/')
def index():
    return render_template('index.html',username=request.cookies.get("username"))

@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = db.session.query(User).filter(User.username==request.form["username"],User.password==request.form["password"]).first()
        if user:
            res = redirect("/")
            username = request.form["username"]
            res.set_cookie("username",username)
            return res
        else:
            return render_template('login.html',error="用户名或者密码错误")

@app.route("/logout/")
def logout():
    res = redirect("/")
    res.delete_cookie("username")
    return res

@app.route("/regist/",methods=["GET","POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)
        db.session.add(User(username,password))
        db.session.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)