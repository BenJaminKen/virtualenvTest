# -*- coding: UTF-8 -*-
class Config:
    #表单需要
    CSRF_ENABLED=True
    SECRET_KEY='BENJAMINDEMO'

    #邮件需要
    MAIL_SERVER='smtp.163.com'
    MAIL_PORT='25'
    MAIL_USE_TLS=True
    MAIL_USERNAME='liuzhiyou_python@163.com'
    MAIL_PASSWORD='uplooking123'

    #数据库需要
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@localhost/devdb?charset=utf8'

class TestConfig(Config):
    TEST=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@localhost/testdb?charset=utf8'

class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@localhost/productdb?charset=utf8'

config={
    'develop':DevelopConfig,
    'test':TestConfig,
    'product':ProductConfig,
    'default':DevelopConfig,
    }
