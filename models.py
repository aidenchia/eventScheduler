from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Faculty(db.Model):
  __tablename__= 'faculty'
  id = db.Column(db.Integer, primary_key=True) # primary keys are unique identifiers
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, id, username, email):
    self.id = id
    self.username = username
    self.email = email

  def __repr__(self):
    return '<Faculty {}>'.format(self.username)

