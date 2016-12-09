import pyrebase
from flask import Flask, render_template, request

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBereFMiEHfkUCgVn11Qyv2vzgOst-TRSM",
    "authDomain": "wtfcolumbia-4dbd1.firebaseapp.com",
    "databaseURL": "https://wtfcolumbia-4dbd1.firebaseio.com/",
    "storageBucket": " wtfcolumbia-4dbd1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

# pr = database.child("posts").get()
# print(pr.val())


@app.route("/")
def index():
    posts_pr = database.child("Post").get()
    posts = []
    for single_post in posts_pr.each():
        data = single_post.val()
        posts.append(data)
    return render_template("index.html", posts=posts)


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts")
def posts():
    posts_pr = database.child("Post").get()
    posts = []
    for single_post in posts_pr.each():
        data = single_post.val()
        posts.append(data)
    return render_template("index.html", posts=posts)


@app.route("/submit_post", methods=['POST'])
def submit_post():
    if request.method == 'POST':
        title = request.form["title_content"]
        post_content = request.form["post_content"]
        tag = request.form["tag_content"]
        upvotes = request.form["upvote_content"]
        downvotes = request.form["downvote_content"]
        d = {"title": title, "post_content": post_content, "tag": tag, "upvotes": upvotes, "downvotes": downvotes}
        database.child("Post").push(d)
    posts_pr = database.child("Post").get()
    posts = []
    for single_post in posts_pr.each():
        data = single_post.val()
        posts.append(data)
    return render_template("index.html", posts=posts)
# @app.route("/post_db", methods=['POST'])
# def post_df():
#   if request.method == "POST":
#       string_content = request.form["comment"]
#       votes = request.form["votes"]
#       dict = {"stringContent": string_content "upvotes":votes}
#       database.
