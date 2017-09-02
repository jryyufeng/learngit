# -*-coding:utf-8-*- 
import pzhn
import mongDB
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
import cloud
import SimilarityDegree
import paint
import shutil #文件模块
import os
import pymongo

from pinyin import PinYin


class Using():
    def __init__(self, topic):
        self.aa=pzhn.get(topic)
        self.xs=SimilarityDegree.XiangSi()
        self.lo1=mongDB.Logger()

    def Analyse(self):
        client = ZhihuClient()
        self.aa.denglu(client)
        self.aa.findquestion(client)
        print'-----------------find','\n'
        list_q = self.aa.Analyse_question(self.aa.dic_name, self.aa.qqcount)
        print'------------------analyse_q','\n'
        self.aa.Analyse_answer(list_q)
        print'--------------------analyse_a','\n'
    def getciyun(self):
        # 得到词云回答者信息
        test1 = PinYin()
        test1.load_word()
        str1 = str(test1.hanzi2pinyin_split(string=str(self.aa.topic), split="-"))
        path1 =  'F:/zhihu/answer/people_qb.txt'
        cloud.ciyun1(path1,str1+'people')
        #得到词云，问题信息
        path2='F:/zhihu/answer/question_top10.txt'
        cloud.ciyun1(path2,str1+'question')
        path2 =  'F:/zhihu/answer/p_location.txt'
        cloud.ciyun1(path2,str1+'slocation')
    def niji(self):
        # 计算回答的基尼系数、
        niji = self.aa.lo.findd("Dic_name", self.aa.topic)
        list_qnum = []
        list_p = []
        list_p.append(1)
        count0 = 0
        aaa=0
        for i in self.lo1.db_table5.find():
           aaa=i['paint']
        for num in niji:
            if num == 0:
                count0 += 1
            list_qnum.append(num)
            list_p.append(float(num)/float(aaa))
        paint.zhitu(list_p)
        print pzhn.gini_coef(list_qnum), "do have answer is:%d" % count0

    def xiangsidu(self):
        lol = mongDB.Logger()
        count = 1
        dic_11={}
        for i in range(10):
            files1 = self.xs.analyse_nr('F:/zhihu/answer1' +str(count)+ '/')
            #print files1
            text = self.xs.change(files1)
            dic_11=self.xs.wordeee(text, self.aa.topic,'F:/zhihu/answer1' +str(count)+ '/'+"q.txt")
            count += 1
        lol.db_table7.insert(dic_11)  ###########
    def all_steps(self):
        #pzh.clean('F:/zhihu/answer1')
        if os.path.exists("F:/zhihu/answer11")==False:
            for i in range(10):
                os.mkdir("F:/zhihu/answer1"+str(i+1))
        if os.path.exists("F:/zhihu/answer11"):
            for i in range(10):
                pzhn.clean("F:/zhihu/answer1"+str(i+1))
        self.Analyse()  # 分析话题下的问题和回答得到，领袖意见/核心问题存入数据库，并形成绘图所需文件
        self.niji()  # 得到尼基系数及劳伦兹曲线
   #     self.getciyun()  # 得到词云
     #   self.xiangsidu()  # 得到高频词汇并存入数据库的Pin表


def detect(topic):
    u = Using(topic)
    u.all_steps()
    return 100


class ZhihuMongo(object):

    def __init__(self):
        self.mongo_client = pymongo.MongoClient('localhost', 27017)
        self.db = self.mongo_client['runoob1']
        self.can_get = 0
        self.has_start_get = 0
        self.topic = ''

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
            detect(topic)
            self.has_start_get = 0
            self.can_get = 1
            return 1

        if self.can_get == 0:
            self.has_start_get = 1
            print(self.has_start_get, self.can_get)
            self.topic = topic
            detect(topic)
            print(self.has_start_get, self.can_get)
            self.has_start_get = 0

            self.can_get = 1
            return 1

    def get_top_people_from_mongodb(self):
        table = self.db['People_top10']
        top_list = []
        for i in table.find():
            if i['topic'] == self.topic:
                for person in i['top']:
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
        return top_list

    def get_all_people_from_mongodb(self):
        table = self.db['People_all']
        all_list = []
        for i in table.find():
            if i['topic'] == self.topic:
                for person in i["person"]:
                    all_list.append(person)
                break
        return all_list


if __name__=='__main__':
    result = detect(topic="林肯公园")
    print result
    # pzh.clean('F:/zhihu/answer1')
    # user = Using()
    # user.Analyse()  # 分析话题下的问题和回答得到，领袖意见/核心问题存入数据库，并形成绘图所需文件
    # user.niji()  # 得到尼基系数及劳伦兹曲线
    # user.getciyun()  # 得到词云
    # final_num=user.xiangsidu()  # 得到高频词汇并存入数据库的Pin表
