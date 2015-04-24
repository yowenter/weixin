#-*-encoding:utf-8-*-
from functools import wraps
from flask import request,abort
from config import ADMIN,PASSWORD

def authorize(f):
    @wraps(f)
    def wrapper(*args,**kargs):
        if request.values.get('admin','')!=ADMIN or request.values.get('password','')!=PASSWORD:
            abort(401)
        return f(*args,**kargs)
    return wrapper



