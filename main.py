from flask import Flask, render_template, request, redirect, url_for
from os import path

app = Flask(__name__)

picFolder = path.join('satic', 'pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    return 'site main'



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'jonas' and password == '1234':
            return redirect('/account')
        else:
            return 'Login Falhou'

    else:
        return render_template('login.html')



@app.route('/account/<username>')
def account(username):
    return render_template('account.html', name=username)




@app.route('/signup')
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "The passwords don't match"

        return redirect('/login')
    else:
        return render_template('signup.html')




@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')




# @app.route('/account')
# def account():
#     return render_template('account.html')




if __name__ == '__main__':
    app.run(debug=True)

