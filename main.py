import json

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    with open("blog-data.json") as blog_file:
        blog_data = json.load(blog_file)
    return render_template("index.html", blog_post=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
