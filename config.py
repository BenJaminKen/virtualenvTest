# -*- coding: UTF-8 -*-
class Config:
    #表单需要
    CSRF_ENABLED=True
    SECRET_KEY='BENJAMINDEMO'

    #邮件需要
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT='587'
    MAIL_USE_TLS=True
    MAIL_USERNAME='804356962@qq.com'
    MAIL_PASSWORD='zpdrhojruxtdbcgh'

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
