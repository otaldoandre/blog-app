from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/5e6358fe9b614917daf4").json()
print(posts)
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"], post["image"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

#Load pages
@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/about')
def show_about():#
    return render_template("about.html")

@app.route('/contact')
def show_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()


