from flask import Flask,render_template,request,make_response,redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler
app=Flask(__name__)
app.secret_key='nowcoder'
@app.route('/')
def index():
    res=''
    for msg,category in get_flashed_messages(with_categories=True):
        res=res+category+msg+'<br>'
    res+='hello'
    return res
@app.route('/profile/<int:uid>/',methods=['post','get'])
def profile(uid):
    colors={'red','green'}
    infos={'a':'baidu','b':'google'}
    return render_template('profile.html',uid=uid,colors=colors,infos=infos)
@app.route('/request')
def request_demo():
     key=request.args.get('key','defaultykey')
     res=request.args.get('key','defaultykey')+'<br>'
     res=res+request.url+'<br>'+request.path+'<br>'
     for prority in dir(request):
         res=res+str(prority)+'|==|'+'<br>'+str(eval('request.'+prority))+'<br>'
     response=make_response(res)
     response.set_cookie('nowcoderid',key)
     response.status='404'
     response.headers['codedd']='hello~~'
     return response
@app.route('/newpath')
def newpath():
    return 'new path'
@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath',code=code)
@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html',url=request.url),404
@app.route('/admin')
def admin():
    key=request.args.get('key','defultykey')
    if key=='admin':
        return 'hello admin'
    else:
        raise Exception()
@app.errorhandler(400)
def exception_page(error):
    return 'exception'
@app.route('/login')
def login():
    app.logger.info('log success')
    flash('succesful','info')
    return redirect('/')
@app.route('/log/<level>/<msg>')
def log(level,msg):
    dict={'warn':logging.WARN,'error':logging.ERROR,'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+msg
def set_logger():
    info_file_handler=RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)

if __name__=='__main__':
    set_logger()
    app.run(debug=True)
