from flask_wtf import  FlaskForm
from wtforms.validators import DataRequired,EqualTo,Length,Email,ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from app.models import User

class LoginForm(FlaskForm):
    email=StringField(label=u'邮箱',validators=[DataRequired(message=u'邮箱必须填写'),Length(1,128,message='长度为1-128'),Email(message=u'邮箱格式不对')])
    password=PasswordField(label=u'密码',validators=[DataRequired(message=u'密码必须填写'),Length(1,128,message=u'长度为1-128')])
    submit=SubmitField(label=u'登陆')

    def validate_email(self,field):
        user=User.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError('此邮箱没有注册')