# -*- coding:utf-8 -*-
from __future__ import print_function, division
import zhihu_oauth
from zhihu_oauth.zhcls import topic, People, Question, SearchResultSection, Answer
import os
import numpy as np
import pymongo
from zhihu_oauth import ZhihuClient
import jieba
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
FENCIPATH='F:/t8/project_name/app_name/ml/'
STOPWORDSPATH = 'F:/t8/project_name/app_name/ml/stopwords_cn.txt'
TOKEN_FILE = 'token.pkl'
DATABASE = "motianji1"
TOPPEOPLE = "top_people"
ALLPEOPLE = "people_all"
ALLQUESTION = "question_all"

def zhihu_login():
    client = ZhihuClient()

    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        client.login('nengtuo310@126.com', 'a4906639')
        client.save_token(TOKEN_FILE)
    me = client.me()
    print(me.name)
    return client


class ZhihuStore(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient('localhost', 27017)
        self.db = self.mongo_client[DATABASE]

    def store_into_mongodb(self, table, dict_info):
        table = self.db[table]
        table.insert(dict_info)

    def get_from_mongodb(self, table, topic):
        table = self.db[table]
        for i in table.find():
            if str(i['topic']) == str(topic):
                return i


def search_process(client, topic="龙珠改魔人布欧"):
    ZhihuStore_object = ZhihuStore()
    people_all_dict = {}
    people_all_dict['topic'] = topic
    people_all_dict['people'] = []

    z_question_count = 0
    z_question_list = []
    z_top_question_dict = {
        "topic": topic,
        "question_list": z_question_list
    }

    for count, result in zip(range(3), client.search(topic, search_type="GENERAL")):
        if not isinstance(result, SearchResultSection):
            # result is SearchResult object
            r = result
            # do something with r
            print(r.obj)
            if isinstance(r.obj, Answer):
                z_answer = r.obj
                try:
                    print(unicode(z_answer.content))
                    z_question = z_answer.question
                    print(unicode(z_question.title))
                except:
                    continue
                z_question_count += 1

                if z_question_count >= 8:
                    break
                z_question_list.append(
                    {
                        "answer_count": int(z_question.answer_count),
                        "question_title": z_question.title,
                        "question_id": z_question.id
                    }
                )
                z_question_list.sort(key=lambda question: question["answer_count"], reverse=True)


                for i, z_answer in zip(range(3), z_question.answers):
                    time.sleep(0.3)
                    person_dict = {}
                    person_dict['name'] = ''
                    person_dict['id'] = ''
                    person_dict['description'] = ''
                    person_dict['business'] = ''
                    person_dict['school'] = ''
                    person_dict['major'] = ''
                    person_dict['job'] = ''
                    person_dict['location'] = ''
                    person_dict['follower_count'] = ''
                    person_dict['following_count'] = ''
                    person_dict['answer_count'] = ''
                    person_dict['this_answer_content'] = strip_content(z_answer.content)
                    person_dict['this_answer_question_title'] = z_question.title
                    person_dict['this_answer_question_id'] = z_question.id
                    person_dict['this_answer_id'] = z_answer.id
                    person_dict['voteup_count'] = z_answer.voteup_count
                    try:
                        print(unicode(z_answer.content))
                    except:
                        continue
                    print("**"*10)
                    if not z_answer.author.over:
                        z_author = z_answer.author
                        print(z_author.name)
                        person_dict['name'] = z_author.name
                        person_dict['id'] = z_author.id
                        person_dict['follower_count'] = z_author.follower_count
                        person_dict['following_count'] = z_author.following_count
                        person_dict['answer_count'] = z_author.answer_count
                        try:
                            if z_author.business:
                                print(z_author.business.name)
                                person_dict['business'] = z_author.business.name
                        except:
                            pass
                        try:
                            if z_author.description:
                                person_dict['description'] = z_author.business.name
                        except:
                            pass
                        try:
                            if z_author.locations:
                                person_dict['location'] = z_author.locations.name
                        except:
                            pass
                        try:
                            for education in z_author.educations:
                                if 'school' in education:
                                    person_dict['school'] = education.school.name
                                if 'major' in education:
                                    person_dict['major'] = education.major.name
                        except:
                            pass

                        people_all_dict['people'].append(person_dict)
                    else:
                        with open("over1.txt", 'a') as f:
                            f.write(str(z_answer.author.over.reason))

        print('-' * 20)

    top_people_dict = {}
    top_people_dict['topic'] = topic
    top_people_list = []
    for person in people_all_dict['people']:
        top_people_list.append(person)
    top_people_list.sort(key=lambda person: person["voteup_count"], reverse=True)
    try:
        top_people_list = top_people_list[:8]
    except:
        pass
    top_people_dict['top_people_list'] = top_people_list



    ZhihuStore_object.store_into_mongodb(table=TOPPEOPLE, dict_info=top_people_dict)
    ZhihuStore_object.store_into_mongodb(table=ALLPEOPLE, dict_info=people_all_dict)
    ZhihuStore_object.store_into_mongodb(table=ALLQUESTION, dict_info=z_top_question_dict)


#                           'ke Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
def zht(url,x):
    x = str(x)
    import urllib2
    import urllib
    from bs4 import BeautifulSoup
    import re
    req=urllib2.Request(url,headers=headers)
    try:
        content=urllib2.urlopen(req,timeout=20).read()
    except Exception,e:
        #print 'time out'+a+b+c
        return False
    print(6666666666666666666666666666666666666666666666666666666666666666666666666666666666)
    print(6666666666666666666666666666666666666666666666666666666666666666666666666666666666)
    with open('F:/sd.txt','a') as f:
        f.write("655t")
    soup=BeautifulSoup(content,'lxml')
    t1=str(soup.find_all(attrs={"class":"Avatar AuthorInfo-avatar"}))
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    img = re.findall(imgre,t1)
    for imgurl in img:
        urllib.urlretrieve(imgurl, 'F:/%s.jpg' % x)
    return True


def get_image_of_top_people(url, index):
    import requests
    from bs4 import BeautifulSoup
    try:
        r_content = requests.get(url, headers=headers, timeout=14).content

        b_content = BeautifulSoup(r_content, "lxml")
        target_href = b_content.find(attrs={"class": "Avatar AuthorInfo-avatar"})["src"]
        t_content = requests.get(target_href, headers=headers, timeout=10).content
        with open('F:/haha'+str(index)+'.jpg', 'wb') as f:
            f.write(t_content)

    except:
        return False





def rm_tokens(words): # 去掉一些停用次和数字
    words_list = list(words)
    stop_words = get_stop_words()
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words: # 去除停用词
            words_list.pop(i)
        elif words_list[i].isdigit():
            words_list.pop(i)
    return words_list


def get_stop_words(path=STOPWORDSPATH):
    file = open(path, 'rb').read().split('\n')
    return set(file)


def get_all_fenci_words(content):
    all_tags = jieba.cut(content)
    all_tags_real = []
    for i in all_tags:
        all_tags_real.append(i)
    all_tags_real = rm_tokens(all_tags_real)
    return all_tags_real


def get_frequent_fenci_words(content):
    tags_real = []
    tags = jieba.analyse.extract_tags(content, topK=12)
    for i in tags:
        tags_real.append(i)
    return tags_real


def get_frequency(all_tags_real, tags):
    count = 0
    num = 0
    for i in tags:
        for j in all_tags_real:
            if i == j:
                count += 1
            num += 1
    print(count)
    print(num)
    if num == 0:
        for i in all_tags_real:
            print(i)
        return 0
    return count/num


def get_high_frequency_vocabulary(topic):

    ZhihuStore_object = ZhihuStore()
    info_dict = ZhihuStore_object.get_from_mongodb(ALLPEOPLE, topic=topic)
    print(info_dict['topic'])
    people_list = []
    for i in info_dict['people']:
        people_list.append(i)
    target_question_dict = ZhihuStore_object.get_from_mongodb(ALLQUESTION, topic=topic)

    target_question_list = []
    for i in target_question_dict['question_list']:
        target_question_list.append(i)

    return_question_list = []

    for question_info in target_question_list:
        return_question_dict = {
            "frequency": 0,
            "words_list": [],
            "question_id": question_info['question_id'],
            "question_title": question_info['question_title'],
        }
        content = ''
        for person in people_list:
            print(int(person['this_answer_question_id']))
            print("--------------------")
            print(int(question_info['question_id']))
            if int(person['this_answer_question_id']) == int(question_info['question_id']):
                print(22222)
                content += person['this_answer_content']
                print(content)
        all_tags_real = get_all_fenci_words(content)
        tags = get_frequent_fenci_words(content)
        return_question_dict["frequency"] = get_frequency(all_tags_real, tags)
        return_question_dict["words_list"] = tags

        return_question_list.append(return_question_dict)
    for i in return_question_list:
        print(i)
    return return_question_list


def strip_content(content):
    import re
    dr = re.compile(r'<[^>]+>', re.S)
    content = dr.sub('', content)
    return content


class ZhihuMongo(object):

    def __init__(self):
        self.mongo_client = pymongo.MongoClient('localhost', 27017)
        self.db = self.mongo_client[DATABASE]
        self.can_get = 0
        self.has_start_get = 0
        self.topic = ''
        self.client = zhihu_login()

    def start_run(self, topic):
        if self.has_start_get == 1:
            return 0
        if self.has_start_get == 0:
            self.has_start_get = 1

        if self.can_get == 1 and self.topic == topic:
            print(self.has_start_get, self.can_get)
            self.has_start_get = 0
            return 1
        if self.can_get == 1 and self.topic != topic:
            print(self.has_start_get, self.can_get)
            print(":ee")
            self.has_start_get = 1
            self.topic = topic
            search_process(self.client, topic=self.topic)
            self.has_start_get = 0
            self.can_get = 1
            return 1

        if self.can_get == 0:
            self.has_start_get = 1
            print(self.has_start_get, self.can_get)
            self.topic = topic
            search_process(self.client, topic=self.topic)
            print(self.has_start_get, self.can_get)
            self.has_start_get = 0

            self.can_get = 1
            return 1

    def get_top_people_from_mongodb(self):
        table = self.db[TOPPEOPLE]
        top_list = []
        for i in table.find():
            if str(i['topic']) == str(self.topic):
                for person in i['top_people_list']:
                    top_list.append(person)
                break
        if len(top_list) > 8:
            top_list = top_list[:8]
        elif len(top_list) < 8:
            while len(top_list) < 8:
                top_list.append(
                    {
                        "name": '暂无',
                        "description": "暂无",
                        "answer_id": "1"
                    }
                )
        for index, value in enumerate(top_list):
            url = 'https://www.zhihu.com/answer/' + str(value['this_answer_id'])
            time.sleep(0.5)
            get_image_of_top_people(url, str(index))
        return top_list

    def get_all_people_from_mongodb(self):
        table = self.db[ALLPEOPLE]
        all_list = []
        for i in table.find():
            if i['topic'] == self.topic:
                for person in i["people"]:
                    all_list.append(person)
                break
        return all_list

    def get_frequent_words(self):
        return get_high_frequency_vocabulary(self.topic)

    def get_business_and_value_from_mongodb(self):
        table = self.db[ALLPEOPLE]
        b_v_list = []
        name_list = []
        for i in table.find():
            if i['topic'] == self.topic:
                for person in i["people"]:
                    if person["business"] != '':
                        b_v_dict = {"name": person["business"], "value": 1}
                        if b_v_dict["name"] in name_list:
                            target_index = name_list.index(b_v_dict["name"])
                            b_v_list[target_index]["value"] += 1
                        else:
                            name_list.append(b_v_dict["name"])
                            b_v_list.append(b_v_dict)
                break
        return b_v_list

    def get_ciyun1(self, type1):
        text = ""
        if str(type1) == str("business"):
            all_list = self.get_all_people_from_mongodb()
            for people in all_list:
                if people["business"]:
                    text = text + " " + str(people["business"])
            if text == "":
                text = "职业数量较少 暂无"
        elif str(type1) == str("location"):
            all_list = self.get_all_people_from_mongodb()
            for people in all_list:
                if people["location"]:
                    text = text + " " + str(people["location"])
            if text == "":
                text = "地点数量较少 暂无"
        elif str(type1) == str("question"):
            question_list = self.get_frequent_words()
            for question in question_list:
                for tag in question["words_list"]:
                    text = text + " " + str(tag)

        wordlist = jieba.cut(text)
        wl_space_split = " ".join(wordlist)
        d = path.dirname(__file__)

        nana_coloring = imread(path.join(d, type1 + ".jpg"))
        my_wordcloud = WordCloud(
            background_color='white',  # 设置背景颜色
            mask=nana_coloring,  # 设置背景图片
            max_words=300,  # 设置最大实现词数
            stopwords=STOPWORDS,  # 设置停用词
            max_font_size=80,  # 设置字体最大值
            random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
            scale=3  # 设置分辨率
        )
        my_wordcloud.generate(wl_space_split)
        image_colors = ImageColorGenerator(nana_coloring)  # 改变字体颜色
        plt.imshow(my_wordcloud)  # 显示词云图
        plt.axis("off")  # 是否显示x轴，y轴下标
        my_wordcloud.to_file(path.join(d, "z_" + type1 + ".jpg"))
#
# def ciyun1(type1, back):
#     text="""g
#     """
#     wordlist=jieba.cut(text)
#     wl_space_split=" ".join(wordlist)
#     d=path.dirname(__file__)
#     if back.find('slocation')!=-1:
#         print('hh')
#         nana_coloring=imread(path.join(d,"location.jpg"))
#     else:
#         nana_coloring = imread(path.join(d, "nihao.jpg"))
#     my_wordcloud=WordCloud(
#         background_color='white',                # 设置背景颜色
#         mask=nana_coloring,                      # 设置背景图片
#         max_words=300,                           # 设置最大实现词数
#         stopwords=STOPWORDS,                     # 设置停用词
#         max_font_size=80,                        # 设置字体最大值
#         random_state=30,                         # 设置有多少种随机生成状态，即有多少种配色方案
#         scale=3                                  # 设置分辨率
#     )
#     my_wordcloud.generate(wl_space_split)
#     image_colors=ImageColorGenerator(nana_coloring)          #改变字体颜色
#     plt.imshow(my_wordcloud)                                  #显示词云图
#     plt.axis("off")                                           #是否显示x轴，y轴下标
#     my_wordcloud.to_file(path.join(d, back+".jpg"))
#




if __name__ == '__main__':
    ciyun1(type1="zhiye", back='23')
    # a = ZhihuMongo()
    # a.start_run("从小开始学语文")
    # a.start_run("从小开始学语文")
    # print(a.get_top_people_from_mongodb())


    # client = zhihu_login()
    # search_process(client, topic="龙珠超")
    # get_high_frequency_vocabulary("龙珠超")

# for result in client.search("水滴直播", search_type="GENERAL"):
#     print(type(result))
#     if isinstance(result, Answer):
#         print(result.type, "people!!!!!!")
#         for r in result:
#             # do something with r
#             print(r.obj)
# for result in client.search_unfold("panda"):
#     # result is SearchResult object
#     r = result
#     print(r.highlight_title, r.highlight_desc)
#     print(r.obj)
#     print('-' * 20)


#
# for question in client.search("水滴直播", search_type='TOPIC'):
#     topic = question.obj
#     for question in topic.unanswered_questions:
#         print(question.title)
    # for act in topic.activities:
    #     if isinstance(act, Question):
    #         print(act.title)
