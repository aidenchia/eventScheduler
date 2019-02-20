from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subjects(db.Model):
  __tablename__= 'Subjects'
  subjectCode = db.Column(db.Float, primary_key=True) # primary keys are unique identifiers
  term = db.Column(db.Integer, nullable=False)

  def __init__(self, subjectCode, term):
    self.subjectCode = subjectCode
    self.term = term

  def __repr__(self):
    return '<SUBJECT {}>'.format(self.subjectCode)



