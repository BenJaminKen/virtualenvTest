from  app import db
from  werkzeug.security import generate_password_hash,check_password_hash
from  flask_login import  UserMixin
from  app import  login_manager

@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(32))
    email=db.Column(db.String(64))
    password_hash=db.Column(db.String(128))

    @property
    def password(self):
        return  AttributeError('password can not read')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

# user=User(name='benjamin')
# user.password='123456'
# user.check_password('123456')==>True
# user.check_password('1236')==>False


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