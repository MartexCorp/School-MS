from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dbconnect import connection
from wtforms import Form
from forms import Registration



app = Flask(__name__)  # "contains 'main' "
app.secret_key = 'oneTWO3.'

#########################################################
#########################################################

###########    DATABASE CONFIGURATIONS   ################



mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


#########################################################
#########################################################
#########################################################


@app.route('/auth', methods=['POST'])  # index page
def auth():

        user = request.form['inputUser']
        pwd = request.form['inputPassword']

        if (user == 'admin') and (pwd == 'admin'):
            return render_template('dashboard.html')
        else:
            error = 'Invalid Username OR Password! Please Try Again.'
            return render_template('login.html', error=error)


@app.route('/')  # index page
def login():
    return render_template('login.html')


@app.route('/dashboard')  # dashboard
def index():
    return render_template('dashboard.html')


@app.route('/finance')  # index page
def finance():
    return render_template('financials.html')


@app.route('/register')  # dashboard
def register():
    return render_template('register.html')


@app.route('/search')  # index page
def search():
    return render_template('search.html')


@app.route('/classlist')  # dashboard
def classlist():
    return render_template('classlist.html')


@app.route('/ssp')  # index page
def ssp():
    return render_template('ssp.html')


@app.route('/about')  # dashboard
def about():
    return render_template('about.html')


@app.route('/contact')  # contact page
def contact():
    return render_template('contact.html')


@app.route('/webportal')  # web partal connection page
def webportal():
    return render_template('web.html')


@app.route('/services')  # services page
def services():
    return render_template('services.html')


@app.route('/extra')  # extras page
def extra():
    return render_template('extra.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
