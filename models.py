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

  @staticmethod
  def insert(subjectCode, term):
    subject = db.session.query(Subjects).filter_by(subjectCode=subjectCode).first()
    if subject is not None:
      return str(subject.term)
    else:
      subject = Subject(subjectCode, term)
      db.session.add(subject)
      db.session.commit()
      print("Added new subject!")
      return str(subject.term)








