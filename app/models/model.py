from .core import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),unique=True)
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Book %r>' % self.title