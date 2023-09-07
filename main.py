from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='/static')

@app.route('/')
def index():
    return 'site main'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'jonas' and password == '1234':
            return 'Login bem-sucedido'
        else:
            return 'Login Falhou'

    else:
        return render_template('login.html')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)

