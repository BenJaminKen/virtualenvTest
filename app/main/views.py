from . import  main
from flask import render_template

@main.route("/",methods=['GET','POST'])
def index():
    info=u'欢迎个锤子'
    return render_template('main/index.html',info=info)

@main.app_errorhandler(404)
def errorhandler_404(e):
    return render_template('error/404.html')

@main.app_errorhandler(500)
def errorhandler_500(e):
    return render_template('error/500.html')