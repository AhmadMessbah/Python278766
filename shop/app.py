from flask import Flask, request, render_template, url_for
import logging

from shop.controller.user_controller import UserController
from shop.model.entity.user import User

app = Flask(__name__,template_folder="view",static_folder="view/assets")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user", methods=["GET","POST","PUT", "DELETE"])
def users():
    if request.method=="POST":
        print(UserController.save( request.form.get("username"),  request.form.get("password")))
    elif request.method =="PUT":
        pass
    elif request.method =="DELETE":
        pass
    return render_template("user.html")


@app.route("/storage", methods=["GET","POST","PUT", "DELETE"])
def storages():
    if request.method=="POST":
        pass
    elif request.method =="PUT":
        pass
    elif request.method =="DELETE":
        pass
    return render_template("storage.html")


@app.route("/invoice", methods=["GET","POST","PUT", "DELETE"])
def invoices():
    if request.method=="POST":
        pass
    elif request.method =="PUT":
        pass
    elif request.method =="DELETE":
        pass
    return render_template("invoice.html")

@app.route("/stuff", methods=["GET","POST","PUT", "DELETE"])
def stuffs():
    if request.method=="POST":
        pass
    elif request.method =="PUT":
        pass
    elif request.method =="DELETE":
        pass
    return render_template("stuff.html")

app.run()


