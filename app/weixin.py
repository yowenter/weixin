# -*- coding: utf-8 -*-
import hashlib
from flask import request,abort
from functools import wraps
from config import WEIXIN_TOKEN


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

    
