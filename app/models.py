from  app import db

class HeadTeacher(db.Model):
    __tablename__='headteachers'
    id=db.Column(db.INTEGER,primary_key=True)
    age=db.Column(db.INTEGER,default=24)
    name=db.Column(db.String(32))

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.INTEGER,primary_key=True)
    age=db.Column(db.INTEGER,default=24)
    name=db.Column(db.String(32))
    teacher_id=db.Column(db.INTEGER,db.ForeignKey('teachers.id'))



class Teacher(db.Model):
    __tablename__='teachers'
    id=db.Column(db.INTEGER,primary_key=True)
    age = db.Column(db.INTEGER, default=44)
    name=db.Column(db.String(32))
    students=db.relationship('Student',backref='teacher')