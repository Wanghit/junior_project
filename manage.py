# -*- encoding=UTF-8 -*-
from flask_script import Manager
from c2 import app

manager=Manager(app)

@manager.option('-n','--name',dest='name',default='noecoder')
def hello(name):
    #嗯嗯
    print 'hello',name

@manager.command
def init_database():
    'init database'
    print 'database...'
if __name__=='__main__':
   manager.run()