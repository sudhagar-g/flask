import os
from datetime import datetime
from flask import Flask, render_template,flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2884384d35cf50674db944425e67c98c'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,'site.db')}"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True, nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'ddd.jpg')
    password = db.Column(db.String(60),nullable =False )
    posts = db.relationship('Post', backref='author', lazy = True)


    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    date_post = db.Column(db.DateTime, nullable=False, default =datetime.utcnow)
    content = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_post}')"




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

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!','success')
            return redirect(url_for('hello'))
        else:
            flash('login unsucessful.please check username and password','danger')
    return render_template("login.html",title="Login",form=form)




if __name__ == "__main__":
   with app.app_context():
       db.create_all()
   app.run(debug=True) 
