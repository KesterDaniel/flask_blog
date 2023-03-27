from flask import Flask, render_template, request
import json
import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

context = ssl.create_default_context()
MY_EMAIL = "kesterdaniel401@gmail.com"
MY_PASSWORD = os.getenv("MY_PASSWORD")


# send mail function
def send_mail(name, email, phone, email_to_send):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{email_to_send}"
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="kesterdan17@gmail.com",
            msg=email_message
        )


@app.route('/')
def home():
    with open("blog-data.json") as blog_file:
        blog_data = json.load(blog_file)
    return render_template("index.html", blog_posts=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    email_sent = False
    if request.method == "GET":
        return render_template("contact.html", email_sent=email_sent)
    else:
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        send_mail(name, email, phone_number, message)
        email_sent = True

        return render_template("contact.html", email_sent=email_sent)


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
