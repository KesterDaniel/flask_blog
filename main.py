import json

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    with open("blog-data.json") as blog_file:
        blog_data = json.load(blog_file)
    return render_template("index.html", blog_posts=blog_data)

@app.route("/readblog/<id>")
def read_blog(id):
    with open("blog-data.json") as blog_file:
        blog_data = json.load(blog_file)
    return render_template("post.html", blog_posts=blog_data, blog_id=id)


if __name__ == "__main__":
    app.run(debug=True)
