#-*-encoding:utf-8-*-
import logging
import xmltodict
from flask import request
from flask import Flask
from werkzeug import datastructures
import weixin
import service


app=Flask('weixin')
app.config.update(dict(DEBUG=True))
LOG=logging.getLogger(__name__)


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
@service.authorize
def admin():
    return 'login ok.'

@app.route('/weixin', methods=['GET'])
@weixin.verify_weixin
def access_verify():
    return request.values.get('echostr')

@app.route('/weixin',methods=['POST'])
@weixin.verify_weixin
def weixin_callback():
    req_xml= xmltodict.parse(request.data)
    return weixin.make_resp(req_xml)
    
        


if __name__=='__main__':
    app.run('0.0.0.0',port=4000)
