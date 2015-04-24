# -*- coding: utf-8 -*-
import hashlib
from config import WEIXIN_TOKEN


def verify_weixin_server(signature,timestamp,nonce):
    sigstr=''.join(sorted([WEIXIN_TOKEN,timestamp,nonce]))
    sig=hashlib.sha1(sigstr).hexdigest()
    if sig==signature:
        return True
    
