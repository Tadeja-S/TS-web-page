# Dogovorjena struktura pri Flask projektih > podmape:
# "templates" (html) in "static" (podmapi: css, img)

# CLASS - MODEL
from flask import Flask, render_template, request

# NEW OBJECT
app = Flask(__name__)

# CONTROLLER - HANDLER
# 127.0.0.1:5000 je lokalni IP naslov našega računalnika, nedostopen drugim
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "GET":
        return render_template("contact.html")
    
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")
        print(contact_name)
        print(contact_email)
        print(contact_message)
        return render_template("confirm.html")

if __name__ == '__main__':
    app.run(use_reloader=True)

