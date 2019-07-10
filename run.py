from app import create_app
from  flask_script import  Manager,Shell
from  app import  db
from flask_migrate import  Migrate,MigrateCommand
import app.models

app=create_app("develop")

manager=Manager(app)

def make_shell_context():
    return dict(app=app,db=db)

migrate=Migrate(app,db)
manager.add_command('shell',Shell(make_shell_context))
manager.add_command('db',MigrateCommand)

DB=app.config.get('DEBUG')
if DB:
    print('app will start')

manager.run()

# app.run(debug=True)