from . import  main
from flask import render_template,request,abort
from flask_login import login_required
from app.models import User


@main.route("/",methods=['GET','POST'])
def index():
    info=u'欢迎个锤子'
    return render_template('main/index.html',info=info)


@main.route('/user_info')
@login_required
def user_info():
    id=request.args.get('id')
    if id is None:
        abort(404)
    user=User.query.get(int(id))
    if user is None:
        abort(404)
    return render_template('main/user_info.html', user=user)

@main.app_errorhandler(404)
def errorhandler_404(e):
    return render_template('error/404.html')

@main.app_errorhandler(500)
def errorhandler_500(e):
    return render_template('error/500.html')