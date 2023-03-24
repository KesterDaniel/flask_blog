import json

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    with open("blog-data.json") as blog_file:
        blog_data = json.load(blog_file)
    return render_template("index.html", blog_posts=blog_data)

@app.route("/readblog/<int:b_id>")
def read_blog(b_id):
    with open("blog-data.json") as blog_file:
        all_blogs = json.load(blog_file)

    for blog in all_blogs:
        if blog["id"] == b_id:
            blog_data = blog

    return render_template("post.html", blog_post=blog_data, blog_id=b_id)


if __name__ == "__main__":
    app.run(debug=True)
