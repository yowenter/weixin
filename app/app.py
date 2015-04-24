#-*-encoding:utf-8-*-

from flask import request
from flask import Flask
from service import authorize
from werkzeug import datastructures

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


@app.route('/admin',methods=['POST','GET'])
@authorize
def admin():
    return 'login ok.'



if __name__=='__main__':
    app.run('0.0.0.0',port=4000)
