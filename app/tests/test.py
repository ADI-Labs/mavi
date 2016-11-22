import pyrebase

config = {
  "apiKey": "AIzaSyAgQ4-daQGKcwN4AFf03VuckQbkiaRgypQ",
  "authDomain": "wtfcolumbia-395d2.firebaseapp.com",
  "databaseURL": "https://wtfcolumbia-395d2.firebaseio.com/",
  "storageBucket": "wtfcolumbia-395d2.appspot.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

ishaan = {
	"firstName" : "Ishaan",
	"lastName": "Agrawal",
	"nickname" : "ia2341",
	"email" : "ia2341@columbia.edu",
	"joinDate" : "10/28/16",
	"school" : "SEAS",
	"year" : "2019",
	"userID" : "#1"
}

comment = {
	"userID" : ishaan["userID"],
	"text" : "This is my first comment.",
	"commentTime" : "5:18:24"
}

post = {
	"title" : "Test",
	"postContent" : "This is the only content",
	"userID" : ishaan["userID"],
	"upvotes" : 10,
	"downvotes" : 3,
	"comments" : comment,
	"uploadTime" : "4:44:59",
	"updateTime" : "",
	"tag" : "#7543"
}

type = {
	"user" :"#1"
}

#database.child("User").push(ishaan)
#database.child("Post").push(post)
database.child("Type").remove()