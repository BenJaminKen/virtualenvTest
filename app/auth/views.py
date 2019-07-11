from . import  auth
from flask import render_template
from  .forms import LoginForm,RegisterForm
from app.models import User
from flask_login import login_user,logout_user,login_required,current_user
from  flask import flash,redirect,url_for
from app import  db
from flask import request,abort



@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user=User(name=form.name.data,email=form.email.data)
        user.password=form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect((url_for('.login')))
    return render_template('auth/register.html',form=form)


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

# @main.app_errorhandler(404)
# def errorhandler_404(e):
#     return render_template('error/404.html')
#
# @main.app_errorhandler(500)
# def errorhandler_500(e):
#     return render_template('error/500.html')