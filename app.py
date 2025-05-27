from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

GIPHY_API_KEY = 'gxlyLldNFwO0rrwFk33iCnLNytnpzkbW'

@app.route("/", methods=["GET", "POST"])
def index():
    gifs = []
    if request.method == "POST":
        termo = request.form["termo"]
        url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={termo}&limit=5&rating=g"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            gifs = [item["images"]["original"]["url"] for item in dados["data"]]
    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)
