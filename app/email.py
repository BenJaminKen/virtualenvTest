from  threading import Thread
from app import config
from app import mail
from flask_mail import Message
from  flask import current_app

def send_fun(app,msg):
    with app.app_context():
        mail.send(msg)

def send_async_main(subject,recvers,body,html):
    app=current_app._get_current_object()
    msg=Message(subject=subject,sender=current_app.config['MAIL_USERNAME'],recipients=recvers)
    msg.body=body
    msg.html=html
    thread=Thread(target=send_fun,args=[app,msg])
    thread.start()