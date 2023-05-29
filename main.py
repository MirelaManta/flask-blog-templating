import requests
from flask import Flask, render_template
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def get_full_post(index):
    post_requested = None
    for blog_post in post_objects:
        if blog_post.id == index:
            post_requested = blog_post
    return render_template("post.html", post=post_requested)


if __name__ == "__main__":
    app.run(debug=True)
