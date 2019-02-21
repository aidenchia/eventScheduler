from flask import Flask
from flask import flash, redirect, render_template, url_for, request, session, abort
from flask_login import login_required
import forms
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print("[INFO] DATABASE_URL:", app.config["SQLALCHEMY_DATABASE_URI"])

from models import db, login_manager
with app.app_context():
  db.init_app(app)
  db.create_all()
  login_manager.init_app(app)
 
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)
 
@app.route('/courseInput', methods=['GET','POST'])
@login_required
def courseInput():
    return render_template('index.html')

@app.route("/logout")
@login_required
def logout():
  session['logged_in'] = False
  return home()

@app.route("/database", methods=['GET','POST'])
@login_required
def display():
  from models import Subjects
  inserted = Subjects.insert(
    request.form['subjectCode'], 
    request.form['term'], 
    request.form['subjectType'], 
    request.form['subjectName'])

  result = Subjects.select(all=True)
  return render_template("database.html", result = result)

@app.route("/export", methods=['GET', 'POST'])
@login_required
def getTable():
  from models import Subjects
  result = Subjects.export(app)
  return result
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)