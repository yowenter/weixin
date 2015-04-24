#-*-encoding:utf-8-*-
import time


TEXT_TEMPLATE = u"""
    <xml>
    <ToUserName><![CDATA[{target}]]></ToUserName>
    <FromUserName><![CDATA[{source}]]></FromUserName>
    <CreateTime>{time}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{content}]]></Content>
    </xml>
    """
def text_reply(target,source,content):
    return TEXT_TEMPLATE.format(target=target,source=source,time=int(time.time()),content=content)




