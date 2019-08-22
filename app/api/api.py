from flask import Blueprint,redirect
from app.models.core import db
from app.models.model import Book
from flask import render_template,request
from .checklogin import checklogin

bp = Blueprint("book",__name__)


@bp.route("/list/")
@checklogin
def list():
    booklist = db.session.query(Book)
    return render_template("list.html", booklist = booklist, user = request.cookies.get("username"))


@bp.route("/detail/<int:id>/")
def detail(id):
    print(id)
    book = db.session.query(Book).filter(Book.id == id).first()
    print(book)

    return render_template("detail.html",  book = book)

@checklogin
@bp.route("/addbook/",methods = ["GET","POST"])
def addbook():
    if request.method == "GET":
        return render_template("addbook.html")
    elif request.method == "POST":
        try:
            bookname = request.form["bookname"]
            db.session.add(Book(bookname))
            db.session.commit()
            return redirect("/list/")
        except Exception as e:
            return render_template("addbook.html", error="添加失败")

@bp.route("/deletebook/<int:id>/", methods=["DELETE"])
def deletebook(id):
    if request.method == "DELETE":
        try:
            book = db.session.query(Book).filter(Book.id==id).first()
            db.session.delete(book)
            db.session.commit()
            return {"code":1}
        except Exception as e:
            print(e)
            return {"code":0}

