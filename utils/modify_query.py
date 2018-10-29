# -*- coding: utf-8 -*-
import os
import json

if __name__ == '__main__':
    # file_name = 'test.txt'
    filename_prefix = "/Users/f7689906/Desktop/python/ner_demo3/data/qurey_prefix.txt"
    filename_songer = "/Users/f7689906/Desktop/python/ner_demo3/data/songer_data.txt"
    filename_music = '/Users/f7689906/Desktop/python/ner_demo3/data/music_data.txt'
    filename_query = '/Users/f7689906/Desktop/python/ner_demo3/data/query.txt'
    filename_music_songer = "/Users/f7689906/Desktop/python/ner_demo3/data/music_songer_name.txt"

    # for prefix in open(filename_prefix):
    #     for songer in open(filename_songer):
    #         # print json.dumps(len(line), encoding="UTF-8", ensure_ascii=False)
    #         for music in open(filename_music):
    #             with open(filename_query, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    #                 f.write(prefix.strip("\n").strip("\t"))
    #                 f.write(songer.strip("\n").strip("\t"))
    #                 f.write("的")
    #                 f.write(music.strip("\n").strip("\n"))
    #                 f.write("\n")

    for music_songer in open(filename_music_songer):
        music_songer = music_songer.split()
        for prefix in open(filename_prefix):
            with open(filename_query, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(prefix.strip("\n").strip("\t"))
                f.write(music_songer[1].strip("\n").strip("\t"))
                f.write("的")
                f.write(music_songer[0].strip("\n"))
                f.write("\n")



