# -*- coding: utf-8 -*-
import hashlib
from flask import request,abort
from functools import wraps
from config import WEIXIN_TOKEN
from  message import text_reply

def verify_weixin(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        signature=request.values.get('signature','')
        timestamp=request.values.get('timestamp','')
        nonce=request.values.get('nonce','')
        sigstr=''.join(sorted([WEIXIN_TOKEN,timestamp,nonce]))
        sig=hashlib.sha1(sigstr).hexdigest()
        if sig==signature:
            return f(*args,**kwargs)
        else:
            abort(401)
    return wrapper

def resp_subsribe(req_data):
    return text_reply(req_data.get('FromUserName'), req_data.get('ToUserName'),"Hello,I am wenter.")

def resp_developing(req_data):
    return text_reply(req_data.get('FromUserName'), req_data.get('ToUserName'),"Well,I am developping...")

def make_resp(req_xml):
    req_data=req_xml.get('xml')
    event=req_data.get('Event')
    if event and 'subscribe' in event:
        return resp_subsribe(req_data)
    else:
        return resp_developing(req_data)
    
        


