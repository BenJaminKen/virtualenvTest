from . import  auth
from flask import render_template
from  .forms import LoginForm,RegisterForm
from app.models import User
from flask_login import login_user,logout_user,login_required,current_user
from  flask import flash,redirect,url_for
from app import  db
from app.email import send_async_main
from flask import request,abort
from  app import  login_manager


@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user=User(name=form.name.data,email=form.email.data)
        user.password=form.password.data
        db.session.add(user)
        db.session.commit()
        token=user.generate_token()
        html = render_template('email/email_confirm.html', token=token, name=user.name)
        send_async_main(subject='本杰明社区',recvers=[user.email],html=html,body=None)
        flash('请登录邮箱验证注册')
        return redirect((url_for('.login')))
    return render_template('auth/register.html',form=form)


@auth.route('/resend_email')
@login_required
def resend_email():
    token = current_user.generate_token()
    html = render_template('email/email_confirm.html', token=token, name=current_user.name)
    send_async_main(subject='本杰明社区', recvers=[current_user.email], html=html, body=None)
    flash('邮件已经重新发送')
    return redirect(url_for('main.user_info',id=current_user.id))


@auth.route('/confirm',methods=['GET','POST'])
@login_required
def confirm():
    token=request.args.get('token')
    if not current_user.check_token(token):
        return render_template('email/email_again.html')
    return redirect(url_for('main.user_info',id=current_user.id))

@auth.route('/request_confirm',methods=['GET','POST'])
def request_confirm():
    return render_template('auth/request_confirm.html')


@auth.before_app_request
def before_app_request():
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint!=None and request.endpoint[:5]!='auth.' and request.endpoint !='static':
        return redirect(url_for('auth.request_confirm'))

@auth.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        user=User.query.filter_by(email=email).first()
        if  user.check_password(password):
            login_user(user)
            return redirect(url_for('main.user_info',id=user.id))
        else:
            flash(u'密码不正确')
    return render_template('auth/login.html',form=form)

@auth.route("/logout",methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect((url_for('.login')))


# 这里需要返回用户  不然就访问不了@login_required
@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))



# @main.app_errorhandler(404)
# def errorhandler_404(e):
#     return render_template('error/404.html')
#
# @main.app_errorhandler(500)
# def errorhandler_500(e):
#     return render_template('error/500.html')