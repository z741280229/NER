# -*- coding: utf8 -*-
if __name__ == '__main__':
    filename_dict = "/Users/f7689906/Desktop/python/ner_demo3/data/music_dict.txt"
    filename_songer = '/Users/f7689906/Desktop/python/ner_demo3/data/songer_data.txt'
    filename_prefix = "/Users/f7689906/Desktop/python/ner_demo3/data/qurey_prefix.txt"
    list_prefix = []
    for prefix in open(filename_prefix):
        list_prefix.append(prefix.strip("\n").strip("\t").strip("\r"))

    for songer in open(filename_songer):
        add_flag = 0
        with open(filename_dict, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                for i in range(len(list_prefix)):
                    songer = songer.strip("\n").strip("\t").strip("\r")
                    if str(list_prefix[i]) == songer:
                       add_flag = add_flag + 1;
                       break
                if  add_flag > 0:
                    continue
                else:
                    f.write(songer)
                    f.write(" ")
                    f.write("nr")
                    f.write("\n")
