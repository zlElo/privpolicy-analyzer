from scraper.webscraper import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        print("Entered link:", link)
        analysis_data = webscrape(link)
        return redirect(url_for('analysis', data=analysis_data))
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    data = request.args.get('data', None)
    return render_template("analysis.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)