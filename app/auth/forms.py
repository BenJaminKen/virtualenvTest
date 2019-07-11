from flask_wtf import  FlaskForm
from wtforms.validators import DataRequired,EqualTo,Length,Email,ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from app.models import User

class LoginForm(FlaskForm):
    email=StringField(label=u'邮箱',validators=[DataRequired(message=u'邮箱必须填写'),Length(1,128,message='长度为1-128'),Email(message=u'邮箱格式不对')])
    password=PasswordField(label=u'密码',validators=[DataRequired(message=u'密码必须填写'),Length(6,128,message=u'长度为6-128')])
    submit=SubmitField(label=u'登陆')

    # 自定义表单验证 方法名为validate+字段名
    def validate_email(self,field):
        user=User.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError('此邮箱没有注册')


class RegisterForm(FlaskForm):

    name = StringField(label=u'昵称', validators=[DataRequired(), Length(1, 128, message='长度为1-128')])
    email=StringField(label=u'邮箱',validators=[DataRequired(message=u'邮箱必须填写'),Length(1,128,message='长度为1-128'),Email(message=u'邮箱格式不对')])
    password=PasswordField(label=u'密码',validators=[DataRequired(message=u'密码必须填写'),Length(6,128,message=u'长度为6-128')])
    password_again = PasswordField(label=u'确认密码',
                             validators=[EqualTo('password',message=u'密码必须填写')])
    submit=SubmitField(label=u'注册')

    # 自定义表单验证 方法名为validate+字段名
    def validate_email(self,field):
        user=User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('此邮箱已经被注册')