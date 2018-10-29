# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == '__main__':
    file_name = "/Users/f7689906/Desktop/python/ner_demo3/data/Musiclib.txt"
    # file_name = 'C:\\Users\\F7688185\\Desktop\\ner_demo\\split_utils\\split_utils\\music\\' + u'旅行.txt'
    filename = '/Users/f7689906/Desktop/python/ner_demo3/data/music_songer.txt'
    count = 0
    num = 0
    for line in open(file_name):
        num = num + 1
        print(num)
        line = line.split()
        if len(line) > 1:
            music = line[0].strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等
            singer = line[1].strip().decode('utf-8', 'ignore')
            p2 = re.compile(ur'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
            zh = " ".join(p2.split(music)).strip()
            zh = ",".join(zh.split())


            zh1 = " ".join(p2.split(singer)).strip()
            zh1 = ",".join(zh1.split())


            new_line = zh  # 经过相关处理后得到中文的文本
            new_songer = zh1


            new_line = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", new_line)
            new_line = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", new_line)

            new_songer = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", new_songer)
            new_songer = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", new_songer)

            with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                if music == new_line:
                    if singer == new_songer:
                        # print(new_songer)
                        # print(new_line)
                      # if count < 20000:
                        f.write(new_line)
                        f.write("\t")
                        f.write(new_songer)
                        f.write("\n")
                        count = count + 1
                      # else:
                      #     break



