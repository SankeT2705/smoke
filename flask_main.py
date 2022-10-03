

from flask import Flask, render_template, request
import prediction as p
import random
app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/page1", methods=["GET", "POST"])
def page1():
    pred = " "
    if request.method == "POST":
        temparature = float(request.form["temp"])
        humidity = float(request.form["Humidity"])
        tvoc = int(request.form["tvoc"])
        eco2 = int(request.form["eCo2"])
        rawh2 = int(request.form["RawH2"])
        raweth = int(request.form["RawEth"])
        pressure = float(request.form["Pressure"])
        pm1 = float(request.form["pm1"])
        pm2 = float(request.form["pm2"])
        nc0 = float(request.form["nc0"])
        nc1 = float(request.form["nc1"])
        nc2 = float(request.form["nc2"])
        cnt = int(request.form["cnt"])

        pred = (p.predict(temparature, humidity, tvoc, eco2, rawh2,
                raweth, pressure, pm1, pm2, nc0, nc1, nc2, cnt))

    print(pred)
    return render_template("page1.html", text=pred)


@app.route("/page2")
def page2():

    return render_template("page2.html")


@app.route("/team")
def team():

    return render_template("team.html")


@app.route("/contact")
def contact():

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
