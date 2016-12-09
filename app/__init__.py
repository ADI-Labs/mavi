from flask import Flask, render_template, request
import pyrebase


app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBereFMiEHfkUCgVn11Qyv2vzgOst-TRSM",
    "authDomain": "wtfcolumbia-4dbd1.firebaseapp.com",
    "databaseURL": "https://wtfcolumbia-4dbd1.firebaseio.com",
    "storageBucket": " wtfcolumbia-4dbd1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

# pr = database.child("posts").get()
# print(pr.val())


@app.route("/")
def index():
    posts_pr = database.child("posts").get()
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
    posts_pr = database.child("posts").get()
    posts = []
    for single_post in posts_pr.each():
        data = single_post.val()
        posts.append(data)
    return render_template("index.html", posts=posts)


@app.route("/submit_post", methods=['POST'])
def submit_post():
    if request.method == 'POST':
        title_content = request.form["title_content"]
        string_content = request.form["post_content"]
        tag_content = request.form["tag_content"]
        upvote_content = request.form["upvote_content"]
        downvote_content = request.form["downvote_content"]
        d = {"title_content": title_content, "string_content":
                string_content, "tag_content": tag_content, "upvote_content":
                upvote_content, "downvote_content": downvote_content}
        database.child("posts").push(d)
    return render_template("index.html")


# @app.route("/post_db", methods=['POST'])
# def post_df():
#   if request.method == "POST":
#       string_content = request.form["comment"]
#       votes = request.form["votes"]
#       dict = {"stringContent": string_content "upvotes":votes}
#       database.
@app.route("/upvotes", methods=['GET', 'POST'])
def upvotes():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        print("here")
        return render_template("index.html")

@app.route("/downvotes", methods=['GET', 'POST'])
def downvotes():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        print("here")
        return render_template("index.html")
