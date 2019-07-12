from  app import db
from  werkzeug.security import generate_password_hash,check_password_hash
from  flask_login import  UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from  flask import current_app



class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(32))
    email=db.Column(db.String(64))
    password_hash=db.Column(db.String(128))
    # 代表用户是否激活
    confirmed=db.Column(db.Boolean,default=False)

    # 生成token,发送邮件验证使用
    def generate_token(self):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=60)
        token = s.dumps({"id":self.id})
        return token

    def check_token(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except:
            return False
        id=data.get('id')
        if id is None:
            return False
        if id!=self.id:
            return False

        self.confirmed = True;
        # db.session.add(self)
        db.session.commit()
        return True


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