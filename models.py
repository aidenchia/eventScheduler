from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subject(db.Model):
  __tablename__= 'SUBJECTS'
  subjectCode = db.Column(db.Float, primary_key=True) # primary keys are unique identifiers
  term = db.Column(db.Integer, nullable=False)

  def __init__(self, subjectCode, term):
    self.subjectCode = subjectCode
    self.term = term

  def __repr__(self):
    return '<SUBJECT {}>'.format(self.subjectCode)

