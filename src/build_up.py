# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
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


# 在不加外词典情况下，不满足为一个词的，添加到外部词典中
def build_up_words():
    filename = '/Users/f7689906/Desktop/python/ner_demo3/data/music_dict.txt'
    words_file = rend_file("/Users/f7689906/Desktop/python/ner_demo3/data/songer_data.txt")
    count = 0
    for i in range(len(words_file)):
        single_word = segmentor_word(words_file[i])
        if len(single_word) > 1:
            count = count + 1
            with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(words_file[i])
                f.write(" ")
                f.write("nr")
                f.write("\n")

    print(count)

# 添加外部词典，查看外部词典可用率
def show_file(path):
    count = 0
    words_file = rend_file(path)
    for i in range(len(words_file)):
        single_word = segmentor_word(words_file[i])
        if len(single_word) > 1:
           print (json.dumps(single_word, encoding="UTF-8", ensure_ascii=False))
           count = count + 1
    print (count)
    print (i)



if __name__ == '__main__':
    words_file = rend_file("/Users/f7689906/Desktop/python/ner_demo3/data/query.txt")
    for i in range(len(words_file)):
        print(words_file[i])
        single_word = abstract_info(words_file[i])
        print(json.dumps(single_word, encoding="UTF-8", ensure_ascii=False))
        print("\n")


    # build_up_words()
    # show_file("/Users/f7689906/Desktop/python/ner_demo3/data/music_dict.txt")
