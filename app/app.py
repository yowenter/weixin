#-*-encoding:utf-8-*-

from flask import request
from flask import Flask,abort
from werkzeug import datastructures
from service import authorize
from weixin import verify_weixin_server

app=Flask('weixin')
app.config.update(dict(DEBUG=True))

@app.before_request
def merge_json():
    json = request.get_json(silent=True)
    if json:
        request.values = datastructures.CombinedMultiDict([request.args,request.form,json])
    else:
        request.values = datastructures.CombinedMultiDict([request.args,request.form])

@app.route('/ping',methods=['GET'])
def ping():
    return "ping ok"
@app.route('/',methods=['GET'])
def index():
    return 'Hey,Taoge!'

@app.route('/admin',methods=['POST','GET'])
@authorize
def admin():
    return 'login ok.'

@app.route('/weixin', methods=['GET'])
def access_verify():
    if not verify_weixin_server(request.values.get('signature',''), request.values.get('timestamp',''), request.values.get('nonce','')):
        abort(401)
    return request.values.get('echostr')
        


if __name__=='__main__':
    app.run('0.0.0.0',port=4000)
