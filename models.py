from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subjects(db.Model):
  __tablename__= 'Subjects'
  subjectCode = db.Column(db.Float, primary_key=True) # primary keys are unique identifiers
  term = db.Column(db.Integer, nullable=True)
  subjectType = db.Column(db.Text, nullable=True)
  subjectName = db.Column(db.Text, nullable=True)

  def __init__(self, subjectCode, term, subjectType, subjectName):
    self.subjectCode = subjectCode
    self.term = term
    self.subjectType = subjectType
    self.subjectName = subjectName

  def __repr__(self):
    return '{}: {}'.format(self.subjectCode, self.subjectName)

  @staticmethod
  def select(all=False):
    if all:
      query = db.session.query(Subjects).order_by(Subjects.subjectName).all()
      return str(query)

    return "TODO"


  @staticmethod
  def insert(subjectCode, term, subjectType, subjectName):
    if None in (subjectCode, term, subjectType, subjectName):
      return "Please fill in all required fields"

    subject = db.session.query(Subjects).filter_by(subjectCode=subjectCode).first()
    if subject is not None:
      result = "{}: {} already in database".format(str(subject.subjectCode), str(subject.subjectName))
      return result
    else:
      subject = Subjects(subjectCode, term, subjectType, subjectName)
      db.session.add(subject)
      db.session.commit()
      result = "Added {}: {} to database".format(str(subject.subjectCode), str(subject.subjectName))
      return result








