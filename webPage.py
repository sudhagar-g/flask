from flask import Flask, render_template,flash, url_for, redirect
from form import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2884384d35cf50674db944425e67c98c'

data = [
    {
        "title":"flask ",
        "author":"Tom",
        "content":"Today i start learn about flask",
        "date_posted":"sep-16-2025 - 5:00pm"
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


@app.route("/register" ,methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect (url_for('hello'))
    return render_template('register.html',title ='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Login",form=form)

if __name__ == "__main__":
    app.run(debug=True) 
