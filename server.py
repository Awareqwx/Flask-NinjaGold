import flask
import random

app = flask.Flask(__name__)
app.secret_key = "RaddaRaddaRadda"

@app.route("/")
def index():
    flask.session.setdefault("gold", 0)
    flask.session.setdefault("acts", [])
    return flask.render_template("index.html", gold=flask.session["gold"], acts=flask.session["acts"])

@app.route("/process_money", methods=["POST"])
def process():
    print int(flask.request.form["goldmax"])
    print int(flask.request.form["goldmin"])
    name = flask.request.form["name"]
    gold = random.randrange(int(flask.request.form["goldmin"]), int(flask.request.form["goldmax"]) + 1)
    flask.session["gold"] += gold
    if name == "Casino":
        if gold != 0:
            flask.session["acts"].append("Entered a casino and " + ("gained " + str(gold) + " gold! Hooray!" if gold > 0 else "lost " + str(-gold) + " gold... Ouch..."))
        else:
            flask.session["acts"].append("Broke even at the casino")
    else:
        flask.session["acts"].append("Earned " + str(gold) + " from the " + name)
    return flask.redirect("/")

@app.route("/reset")
def reset():
    flask.session.pop("acts")
    flask.session.pop("gold")
    return flask.redirect("/")
app.run(debug=True)