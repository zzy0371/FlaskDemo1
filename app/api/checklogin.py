from flask import request,redirect
def checklogin(f):
    def check(*args):
        username = request.cookies.get("username")
        if username:
            return f(*args)
        else:
            return redirect("/login/")
    return check