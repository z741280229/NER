# -*- coding: utf8 -*-
#==============================
file_name = '/Users/f7689906/Desktop/python/ner_demo3/data/music_songer.txt'
#==============================

open('/Users/f7689906/Desktop/python/ner_demo3/data/music_songer_name.txt','w').truncate()

with open(file_name, 'r') as f:
    lines = f.readlines()
print 'lines = ' + str(len(lines))

x = 0

while x < len(lines):

    file = open('/Users/f7689906/Desktop/python/ner_demo3/data/music_songer_name.txt', 'r')
    quchong = file.read()
    file.close()

    if lines[x] not in quchong:
        print '[' + str(x+1) + ']' + 'ok, add'
        file = open('/Users/f7689906/Desktop/python/ner_demo3/data/music_songer_name.txt', 'a')
        file.write(lines[x])
        file.close
    else:
        print '[' + str(x+1) + ']' + 'no, del:' + lines[x].replace('\n','')

    x= x + 1
