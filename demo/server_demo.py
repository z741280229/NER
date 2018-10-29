# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime
import time
import datetime
import sys
import json
import jieba
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding('utf8')
#sys.path.append("../data/")
jieba.load_userdict("/Users/f7689906/Desktop/python/ner_demo3/data/music_dict.txt")

#读取问文本
def rend_file(path):
    file_list = []
    f = open(path)  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        str_deal = line.strip('\n').strip('\t').strip('\r')
        file_list.append(str_deal)
        line = f.readline()
    f.close()
    return file_list

# 分词
def segmentor_word(word):
    terms = jieba.cut(word)
    words_list = list(terms)
    #print(json.dumps(words_list, encoding="UTF-8", ensure_ascii=False))
    return words_list

def abstract_info(query):

    reply_info = []
    words = pseg.cut(query)
    for word, flag in words:
        if flag == "nz":
            print(word,flag)
            reply_info.append(word)
        elif flag == "nr":
            print(word,flag)
            reply_info.append(word)
    return reply_info




host = '127.0.0.1'
port = 21999
addr = (host, port)

class Servers(SRH):
    def handle(self):
        print ('got connection from ', self.client_address)
        self.wfile.write('connection %s:%s at %s succeed!' % (host, port, ctime()))

        while True:
            print(datetime.datetime.now())
            # data = "服务端做出相应"
            data = self.request.recv(1024)
            reply = []
            reply = abstract_info(data)
            deal_reply = "\t"
            deal_reply = deal_reply.join(reply)

            if not data:
                break
            # print data
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print ("%s RECV from %s, data is:%s" % (cur_time, self.client_address[0], data))
            self.request.send(deal_reply)


print ('server is running....')
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()