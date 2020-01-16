import itchat
import time
from itchat.content import *


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'], msg.user)
    if msg.user.UserName == 'filehelper':
        itchat.send('Hello, filehelper', toUserName=msg.user.UserName)


itchat.auto_login(hotReload=True)
itchat.run()
