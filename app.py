from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'hello {guest} as guest'

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest =name))

# redirecting to external page, useful for react pages calling with flask
@app.route('/cart')
def hello_user1():
    return redirect("http://localhost:3000/")

@app.route('/temp')
def temp():
    return render_template('index.html')
   

@app.route('/<name>')
def hello2(name):
    return f'hello {name}'

if __name__ == '__main__':
    app.run(debug=True)