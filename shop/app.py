from flask import Flask, request, render_template, url_for
import logging

app = Flask(__name__,template_folder="view",static_folder="view/static")

@app.route("/")
def home():
    return render_template("index.html")



app.run()


