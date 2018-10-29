#coding:utf-8
from socket import *
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

host = '127.0.0.1'
port = 21999
bufsize = 1024
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
print client.recv(bufsize)
while True:
    data = raw_input()
    if not data or data == 'exit':
        break
    msg = '%s' % data
    client.send(msg)
    data = client.recv(bufsize)
    if not data:
        break
        # print data.strip()
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print ("%s receice from server :%s") % (cur_time,data)
    print(datetime.datetime.now())
client.close()
