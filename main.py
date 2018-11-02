from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("user.html")

@app.route("/", methods=['POST'])
def username():

    error = redirect("/?error=invalid_input")

    username = request.form['username']
    password = request.form['password']
    pass_conf = request.form['pass_conf']
    email = request.form['email']

    username_error = ''
    password_error = ''
    pass_conf_error = ''
    email_error = ''

    if username == "":
        username_error = "Please enter a valid input."
    
    if len(username) < 3 or len(username) > 20:
        username_error = "Your username must be between 3 and 20 characters long."

    if ' ' in username:
        username_error = "No spaces in your username, please."

    if password == "" or pass_conf == "":
        password_error = "Please enter a valid password."
        pass_conf_error = "Please enter a valid password."

    if len(password) < 3 or len(password) > 20:
        password_error = "Your password must be between 3 and 20 characters long."

    if password != pass_conf:
        pass_conf_error = "Please make sure your passwords match."
        password_error = "Please make sure your passwords match."

    if len(email) < 3 or len(email) > 20:
        email_error = "Email must be between 3-20 characters."

    if len(email) > 0 and '@' not in email or '.' not in email :
        email_error = "Please make sure your email contians one period and one @."

    if email.count('@') > 1 or email.count('.') > 1:
        email_error = "Only one ampersand and one period in your email please."

    if username_error == False:
        username = username 
    
    if len(email) == 0:
        email_error = ''
        email = email

    if not username_error and not email_error and password != pass_conf:
        return render_template("user.html",password_error=password_error,pass_conf_error=pass_conf_error,
        username=username, email=email, password='', pass_conf='')

    if not username_error and not email_error and not password_error and not pass_conf_error:
        return render_template("welcome.html",username=username,password=password,pass_conf=pass_conf,email=email)

    
    return render_template("user.html",username=username, username_error=username_error, password=password, password_error=password_error,
    pass_conf=pass_conf,pass_conf_error=password_error,email=email,email_error=email_error)

app.run()