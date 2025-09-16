from flask import Flask, render_template, url_for

app = Flask(__name__)

data = [
    {
        "title":"flask ",
        "author":"Tom",
        "content":"Today i start learn about flask",
        "date_posted":"sep-16-2025 - 5:0pm"
    },
    {
        "title":"Again flask",
        "author":"Tom",
        "content":"""I learned about little bit flask
                     and template""",
        "date_posted":"sep-16-2025 - 8:22pm"

    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('hello.html',posts=data)

@app.route("/about")
def about():
    return render_template("about.html",title="about")

if __name__ == "__main__":
    app.run(debug=True)
