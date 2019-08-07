# -*- coding: utf-8  -*-
# 逐行读取文件数据进行jieba分词

import jieba
import jieba.analyse
import jieba.posseg as pseg #引入词性标注接口 
import codecs,sys


if __name__ == '__main__':
    f = codecs.open('zhwiki.zh.text', 'r', encoding='utf8')
    target = codecs.open('wiki.zh.text.seg', 'w', encoding='utf8')
    print('open files.')

    lineNum = 1
    line = f.readline()
    print("打印line：", line)
    while line:
        print('---processing ',lineNum,' article---')
        seg_list = jieba.cut(line,cut_all=False)
        line_seg = ' '.join(seg_list)
        print("分词", line_seg)
        target.writelines(line_seg)
        lineNum = lineNum + 1
        line = f.readline()
    print('well done.')
    f.close()
    target.close()
