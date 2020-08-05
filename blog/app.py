from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}".format(self.firstname[0], self.lastname[0])

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                            user=User("Drew","Perkins"))

@app.route("/cool_form", methods=["GET", "POST"])
def cool_form():
    if request.method == "POST":
        return redirect(url_for("index"))

    return render_template("cool_form.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)