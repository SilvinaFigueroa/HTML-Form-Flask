# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request

import fortune_results

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/Fortune', methods=['POST', 'GET'])
def fortune():
    if request.method == 'POST':
        user_name = request.form['user']
        user_color = request.form['color']
        user_number = request.form['number']

        return redirect(url_for('user_fortune', user=user_name, color=user_color, number=user_number))

    else:

        user_name = request.args.get('user')
        user_color = request.args.get('color')
        user_number = request.args.get('number')
        return redirect(url_for('user_fortune', user=user_name, color=user_color, number=user_number))


@app.route('/YourFortune/<user>/<color>/<number>')
def user_fortune(user, color, number):
    # return 'Your Fortune: {} {} {}'.format(user, color, number)
    response = fortune_results.results(user, color, number)
    return response


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
