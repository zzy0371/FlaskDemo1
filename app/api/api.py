from flask import Blueprint
from app.models.core import db
from app.models.model import Book
from flask import render_template
from .checklogin import checklogin

bp = Blueprint("book",__name__)


@bp.route("/list/")
@checklogin
def list():
    booklist = db.session.query(Book)
    return render_template("list.html", booklist = booklist)


@bp.route("/detail/<int:id>/")
def detail(id):
    print(id)
    book = db.session.query(Book).filter(Book.id == id).first()
    print(book)

    return render_template("detail.html",  book = book)