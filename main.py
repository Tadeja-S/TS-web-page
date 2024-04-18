# Dogovorjena struktura pri Flask projektih > podmape:
# "templates" (html) in "static" (podmapi: css, img)

# CLASS - MODEL
from flask import Flask, render_template

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

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(use_reloader=True)

