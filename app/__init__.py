from flask import  Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import  Bootstrap
from flask_moment import Moment

#这个变量必须叫做moment和bootstrap
moment=Moment()
bootstrap=Bootstrap()
mail=Mail()
db = SQLAlchemy()
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])

    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    # db.create_all()
    #注册蓝图
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    #绑定app
    return app
