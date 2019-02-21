from flask import Flask
from flask import flash, redirect, render_template, url_for, request, session, abort
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print("[INFO] DATABASE_URL:", app.config["SQLALCHEMY_DATABASE_URI"])
print("[INFO] DEBUG MODE = ",app.config["DEBUG"])

from models import db
with app.app_context():
  db.init_app(app)
  db.create_all()
 
@app.route('/')
def home():
  if not session.get('logged_in'): # if not logged in
    return render_template('login.html')
  else: # if logged in already
    return "Logged In"
 
@app.route('/login', methods=['GET','POST'])
def do_admin_login():
  if request.form['password'] == 'password' and request.form['username'] == 'admin':
    session['logged_in'] = True
    return render_template('index.html')
  else:
    flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
  session['logged_in'] = False
  return home()

@app.route("/database", methods=['GET','POST'])
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
def getTable():
  from models import Subjects
  result = Subjects.export(app)
  return result
 
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)