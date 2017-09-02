# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba.analyse

if __name__ == '__main__':
    with open('sb.txt','r') as f:
        content = f.read()
    tags = jieba.analyse.extract_tags(content, topK=80)
    all_tags = jieba.cut(content)
    all_tags_real = []
    for all_word in all_tags:
        all_tags_real.append(all_word)
    count = 0
    for i in tags:
        print i
        print "----------------"
        for j in all_tags_real:
            print j
            if i==j:
                count += 1



    print(count)
    print(len(all_tags_real))