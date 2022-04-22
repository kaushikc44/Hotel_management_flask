from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import  db
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST" :
        email = request.form.get('emailsignup')
        first_name = request.form.get("firstname")
        password = request.form.get("passwordsignup")
        user = User.query.filter_by(email=email).first()
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
        print(email, password,first_name)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/auth/signup")



    return render_template("signup.html",boolean=True)



@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        emaillogin = request.form.get('emailsignin')
        passwordlogin = request.form.get("passowordsignin")
        user = User.query.filter_by(email=emaillogin).first()
        print(emaillogin,passwordlogin)
        if user:
            if check_password_hash(user.password,passwordlogin):
                login_user(user,remember=True)
                print("Successful password!")
                return redirect(url_for("views.home"))
            else:
                print("Wrong password!")
        else:
            print("User does not exist!")



    return render_template("Login.html",boolean=True)