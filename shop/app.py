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
        pass
    elif request.method =="PUT":
        pass
    elif request.method =="DELETE":
        pass
    return render_template("user.html")

app.run()


