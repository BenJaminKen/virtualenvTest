from . import  auth
from flask import render_template
from  .forms import LoginForm
from app.models import User
from flask_login import login_user,logout_user,login_required
from  flask import flash,redirect,url_for

@auth.route("/login",methods=['GET','POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        user=User.query.filter_by(email=email).first()
        if  user.check_password(password):
            login_user(user)
            return redirect(url_for('.user_info'))
        else:
            flash(u'密码不正确')
    return render_template('auth/login.html',form=form)


@auth.route('/user_info')
@login_required
def user_info():
    return 'OK'

# @main.app_errorhandler(404)
# def errorhandler_404(e):
#     return render_template('error/404.html')
#
# @main.app_errorhandler(500)
# def errorhandler_500(e):
#     return render_template('error/500.html')