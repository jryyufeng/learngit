# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.http import JsonResponse
from django.http import HttpResponse
from ml.realtime_random_weibo_2 import RealtimeRandomWeibo
from zhihu.start_crawl import *

realtime_object_1 = RealtimeRandomWeibo()
zhihumongo_object_1 = ZhihuMongo()

def hello(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    # return render_to_response('hello.html', RequestContext(request))
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    List = [
        [{'name': '北京'}, {'name': '延安', 'value': 98}],
        [{'name': '北京'}, {'name': '咸阳', 'value': 96}],
    ]
    return render(request, 'hello.html', {
            'List': json.dumps(List)
        })

def table(request):         #之前测试的列表
    List = [{"user_email": "7744.rikon@gmail.com", "user_company": "", "user_dates": "2014-10-13 13:35:51",
      "user_lastlogintime": "0", "user_version": "0", "user_isv2": "0", "userstatus_usertype": "0",
      "userstatus_package_id": "100014", "userstatus_end_time": "NULL"},
     {"user_email": "8866@xxxxddffg.com", "user_company": "NULL", "user_dates": "2014-10-13 13:35:51",
      "user_lastlogintime": "0", "user_version": "1", "user_isv2": "0", "userstatus_usertype": "0",
      "userstatus_package_id": "100001", "userstatus_end_time": "NULL"}]
    return render(request, 'demo2-export.html', {
            'List': json.dumps(List)
        })

def weiborelation(request,a):       #之前测试的微博关系图
    List1 = [     {
            "name": "霍霍然",
            "keyword": {},
            "base": "霍霍然"
        }  ,
		        {
            "name": "moef善",
            "keyword": {},
            "base": "moef善"
        },
				        {
            "name": "二ef",
            "keyword": {},
            "base": "二ef"
        }

		]
    List2= [{
         "name": "淤然丫头", # 节点名称
     "value": 100,
              "category": 0 # 与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "李新忠MTNS",
        "value": 10,
        "category": 0
    },
    {
        "name": "幻想曲2010",
        "value": 10,
        "category": 0
    },
    {
        "name": "小兽201409",
        "value": 15,
        "category": 0
    },
    {
        "name": "少年朕要淡定",
        "value": 10,
        "category": 0
    },
    {
        "name": "90后的晓庆6666688",
        "value": 100,
        "category": 0
    },
    {
        "name": "姑姑是过儿啊",
        "value": 17,
        "category": 0
    },
    {
        "name": "kaloo1981_392",
        "value": 21,
        "category": 0
    },
    {
        "name": "某某hom",
        "value": 54,
        "category": 0
    },
    {
        "name": "优位停车车牌识别",
        "value": 20,
        "category": 0
    },
    {
        "name": "犀利哥呼延叔盛胞鞠",
        "value": 60,
        "category": 0
    }, {
        "name": "momokome明远善", # 节点名称
    "value": 100,
             "category": 1 #与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "朿竹2012",
        "value": 42,
        "category": 1
    },
    {
        "name": "世界里的祺365",
        "value": 20,
        "category": 1
    },
    {
        "name": "璐非露201606",
        "value": 32,
        "category": 1
    },
    {
        "name": "嘎哈GAHA",
        "value": 15,
        "category": 1
    },
    {
        "name": "被占据的幸福201607",
        "value": 10,
        "category": 1
    },
    {
        "name": "TR0Y1994",
        "value": 54,
        "category": 1
    },
    {
        "name": "雅思GRE托福GMAT网络课程团购",
        "value": 47,
        "category": 1
    },
    {
        "name": "赠友人三首918",
        "value": 45,
        "category": 1
    },
    {
        "name": "lllllyz哲",
        "value": 20,
        "category": 1
    },
    {
        "name": "ACGS漫展策划官博",
        "value": 12,
        "category": 1
    }, {
        "name": "二次元桃偃", # 节点名称
    "value": 100,
             "category": 2 # 与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "Leslie和爱吃面的铃铛",
        "value": 42,
        "category": 2
    },
    {
        "name": "Bowllo_",
        "value": 35,
        "category": 2
    },
    {
        "name": "北海迷路青年旅舍",
        "value": 37,
        "category": 2
    },
    {
        "name": "鵬_SAMA",
        "value": 50,
        "category": 2
    },
    {
        "name": "面面夏呀",
        "value": 70,
        "category": 2
    },
    {
        "name": "烟檯无痕接发",
        "value": 15,
        "category": 2
    },
    {
        "name": "Amseram",
        "value": 21,
        "category": 2
    },
    {
        "name": "金牌护肤导师筱雨",
        "value": 10,
        "category": 2
    },
    {
        "name": "住二楼的小仙女丹姐姐",
        "value": 20,
        "category": 2
    },
    {
        "name": "Maybe201003",
        "value": 20,
        "category": 2
    }]
    List3 =  [        {
            "source": 0,#起始节点，0表示第一个节点
            "target": 1 #目标节点，1表示与索引为1的节点进行连接
        },
        {
            "source": 0,
            "target": 2
        },
		        {
            "source": 0,
            "target": 3
        },
		        {
            "source": 0,
            "target": 4
        },		        {
            "source": 0,
            "target": 5
        }, 		        {
            "source": 0,
            "target": 6
        }, 		        {
            "source": 0,
            "target": 7
        }, 		        {
            "source": 0,
            "target": 8
        }, 		        {
            "source": 0,
            "target": 9
        },{
            "source": 0,
            "target": 10
        },	{
            "source": 11,#起始节点，0表示第一个节点
            "target": 12 #目标节点，1表示与索引为1的节点进行连接
        },
        {
            "source": 11,
            "target": 13
        },
		        {
            "source": 11,
            "target": 14
        },
		        {
            "source": 11,
            "target": 15
        },		        {
            "source": 11,
            "target": 16
        }, 		        {
            "source": 11,
            "target": 17
        }, 		        {
            "source": 11,
            "target": 18
        }, 		        {
            "source": 11,
            "target": 19
        }, 		        {
            "source": 11,
            "target": 20
        },{
            "source": 11,
            "target": 21
        },{
            "source": 22,#起始节点，0表示第一个节点
            "target": 23 #目标节点，1表示与索引为1的节点进行连接
        },
        {
            "source": 22,
            "target": 24
        },
		        {
            "source": 22,
            "target": 25
        },
		        {
            "source": 22,
            "target": 26
        },		        {
            "source": 22,
            "target": 27
        }, 		        {
            "source": 22,
            "target": 28
        }, 		        {
            "source": 22,
            "target": 29
        }, 		        {
            "source": 22,
            "target": 30
        }, 		        {
            "source": 22,
            "target": 31
        }]
    List4 = ['霍霍然', 'moef善', '二ef']
    if a==1:
        List1 = [{
            "name": "qwe",
            "keyword": {},
            "base": "qwe"
        },
            {
                "name": "asd",
                "keyword": {},
                "base": "asd"
            },
            {
                "name": "zxc",
                "keyword": {},
                "base": "zxc"
            }

        ]
    print  'a  is  '+ a +"---------------------------------"
    return render(request, 'weiborelathion.html', {
            'List1': json.dumps(List1),
        'List2': json.dumps(List2),
        'List3': json.dumps(List3),
        'List4': json.dumps(List4)
        })

def zhihurelation(request):   #之前测试的知乎关系图
    List1 = [{
                 "name": "翟振轶律师", # 关系网名称
             "keyword": {},
                        "base": "翟振轶律师"
    },
    {
        "name": "胡尊杰", # 关系网名称
    "keyword": {},
               "base": "胡尊杰"
    },
    {
        "name": "肖查宁", # 关系网名称
    "keyword": {},
               "base": "肖查宁"
    }

    ]
    List2 = [{
                 "name": "翟振轶律师", # 节点名称
             "value": 100,
                      "category": 0 # 与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "谢金娣",
        "value": 10,
        "category": 0
    },
    {
        "name": "大实话",
        "value": 10,
        "category": 0
    },
    {
        "name": "法盲",
        "value": 10,
        "category": 0
    },
    {
        "name": "大风过后可",
        "value": 10,
        "category": 0
    },
    {
        "name": "今夜月色很好",
        "value": 100,
        "category": 0
    },
    {
        "name": "唯爱金白沙",
        "value": 12,
        "category": 0
    },
    {
        "name": "tommoc",
        "value": 41,
        "category": 0
    },
    {
        "name": "晓风",
        "value": 50,
        "category": 0
    },
    {
        "name": "郭丹",
        "value": 10,
        "category": 0
    },
    {
        "name": "韩同雪",
        "value": 10,
        "category": 0
    }, {
        "name": "胡尊杰", # 节点名称
    "value": 100,
             "category": 1 # 与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "张少壮",
        "value": 72,
        "category": 1
    },
    {
        "name": "bmw li",
        "value": 30,
        "category": 1
    },
    {
        "name": "AKI",
        "value": 27,
        "category": 1
    },
    {
        "name": "修远兮",
        "value": 55,
        "category": 1
    },
    {
        "name": "轩辕偏胖",
        "value": 100,
        "category": 1
    },
    {
        "name": "如题",
        "value": 12,
        "category": 1
    },
    {
        "name": "李猜猜",
        "value": 41,
        "category": 1
    },
    {
        "name": "梁超",
        "value": 50,
        "category": 1
    },
    {
        "name": "川南",
        "value": 10,
        "category": 1
    },
    {
        "name": "yandeqiang",
        "value": 10,
        "category": 1
    }, {
        "name": "肖查宁", # 节点名称
    "value": 100,
             "category": 2 # 与关系网类别索引对应，此处只有一个关系网所以这里写0
    },
    {
        "name": "无印良品",
        "value": 72,
        "category": 2
    },
    {
        "name": "陈文星",
        "value": 30,
        "category": 2
    },
    {
        "name": "枪神周润发",
        "value": 27,
        "category": 2
    },
    {
        "name": "二西复之",
        "value": 55,
        "category": 2
    },
    {
        "name": "bafguy",
        "value": 100,
        "category": 2
    },
    {
        "name": "Lobster",
        "value": 12,
        "category": 2
    },
    {
        "name": "高松波",
        "value": 41,
        "category": 2
    },
    {
        "name": "雨霖",
        "value": 50,
        "category": 2
    },
    {
        "name": "刘震宇",
        "value": 10,
        "category": 2
    },
    {
        "name": "yandeqiang",
        "value": 10,
        "category": 2
    }]

    List3 = [{
                 "source": 0, # 起始节点，0
    "target": 1 # 目标节点，1表示与索引为1的节点进行连接
    },
    {
        "source": 0,
        "target": 2
    },
    {
        "source": 0,
        "target": 3
    },
    {
        "source": 0,
        "target": 4
    }, {
        "source": 0,
        "target": 5
    }, {
        "source": 0,
        "target": 6
    }, {
        "source": 0,
        "target": 7
    }, {
        "source": 0,
        "target": 8
    }, {
        "source": 0,
        "target": 9
    }, {
        "source": 0,
        "target": 10
    }, {
        "source": 11, # 起始节点，0表示第一个节点
    "target": 12 # 目标节点，1表示与索引为1的节点进行连接
    },
    {
        "source": 11,
        "target": 13
    },
    {
        "source": 11,
        "target": 14
    },
    {
        "source": 11,
        "target": 15
    }, {
        "source": 11,
        "target": 16
    }, {
        "source": 11,
        "target": 17
    }, {
        "source": 11,
        "target": 18
    }, {
        "source": 11,
        "target": 19
    }, {
        "source": 11,
        "target": 20
    }, {
        "source": 11,
        "target": 21
    }, {
        "source": 22, # 起始节点，0表示第一个节点
    "target": 23 # 目标节点，1表示与索引为1的节点进行连接
    },
    {
        "source": 22,
        "target": 24
    },
    {
        "source": 22,
        "target": 25
    },
    {
        "source": 22,
        "target": 26
    }, {
        "source": 22,
        "target": 27
    }, {
        "source": 22,
        "target": 28
    }, {
        "source": 22,
        "target": 29
    }, {
        "source": 22,
        "target": 30
    }, {
        "source": 22,
        "target": 31
    }]
    List4 = ['翟振轶律师', '胡尊杰', '肖查宁']

    return render(request, 'zhihurelation.html', {
            'List1': json.dumps(List1),
        'List2': json.dumps(List2),
        'List3': json.dumps(List3),
        'List4': json.dumps(List4)
        })



def data1(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    # return render_to_response('hello.html', RequestContext(request))
    weibo_list = realtime_object_1.get_realtime_weibo_from_mongodb()
    for weibo in weibo_list:
        if weibo['is_repost']:
            weibo['is_repost'] = 1
        else:
            weibo['is_repost'] = 0
        weibo['id'] = weibo['uid']
        weibo['author'] = weibo['author_name']
        weibo['content'] = weibo['text']
        weibo['_id'] = '0'


    return render(request, 'Real-time_monitor.html', {
            'weibo_list': json.dumps(weibo_list)
        })


def monitor(request):       #检测的地图
    List1 = []
    List2 = []
    weibo_list = realtime_object_1.get_realtime_weibo_from_mongodb()
    for weibo in weibo_list:
        if weibo['is_repost']:
            List1.append(
                [
                    {'name': weibo['location']},
                    {'name': weibo['repost_location'], 'value': int(weibo['threatened'])}
                ]
            )
        else:
            List2.append(
                {'name': weibo['location'], 'value': int(weibo['threatened'])}
            )
    # for weibo in weibo_list:
    #     if weibo['is_repost']:
    #         weibo['is_repost'] = 1
    #     else:
    #         weibo['is_repost'] = 0
    #     weibo['id'] = weibo['uid']
    #     weibo['author'] = weibo['author_name']
    #     weibo['content'] = weibo['text']
    #     weibo['_id'] = '0'
    #
    # List1 = 	[	[{'name':'佛山'}, {'name':'北京','value':15}],
		# [{'name':'沈阳'}, {'name':'厦门','value':49}],
		# [{'name':'上海'}, {'name':'北京','value':62}],
		# [{'name':'上海'}, {'name':'北京','value':56}],
		# ]
    # List2 = [
		# 			{'name':'佛山','value':15},
		# 			{'name':'沈阳','value':49},
		# 			{'name':'上海','value':62},
		# 			{'name':'上海','value':56},
		# 			]
    id1 = weibo_list[0]['author_uid']
    author1 = weibo_list[0]['author_name']
    location1 = weibo_list[0]['location']
    time1 = weibo_list[0]['time']
    content1 = weibo_list[0]['text']
    id2 = weibo_list[1]['author_uid']
    author2 = weibo_list[1]['author_name']
    location2 = weibo_list[1]['location']
    time2 = weibo_list[1]['time']
    content2 = weibo_list[1]['text']
    id3 = weibo_list[2]['author_uid']
    author3 = weibo_list[2]['author_name']
    location3 = weibo_list[2]['location']
    time3 = weibo_list[2]['time']
    content3 = weibo_list[2]['text']
    id4 = weibo_list[3]['author_uid']
    author4 = weibo_list[3]['author_name']
    location4 = weibo_list[3]['location']
    time4 = weibo_list[3]['time']
    content4 = weibo_list[3]['text']
    id5 = weibo_list[4]['author_uid']
    author5 = weibo_list[4]['author_name']
    location5 = weibo_list[4]['location']
    time5 = weibo_list[4]['time']
    content5 = weibo_list[4]['text']
    id6 = weibo_list[5]['author_uid']
    author6 = weibo_list[5]['author_name']
    location6 = weibo_list[5]['location']
    time6 = weibo_list[5]['time']
    content6 = weibo_list[5]['text']
    id7 = weibo_list[6]['author_uid']
    author7 = weibo_list[6]['author_name']
    location7 = weibo_list[6]['location']
    time7 = weibo_list[6]['time']
    content7 = weibo_list[6]['text']
    id8 = weibo_list[7]['author_uid']
    author8 = weibo_list[7]['author_name']
    location8 = weibo_list[7]['location']
    time8 = weibo_list[7]['time']
    content8 = weibo_list[7]['text']
    id9 = weibo_list[8]['author_uid']
    author9 = weibo_list[8]['author_name']
    location9 = weibo_list[8]['location']
    time9 = weibo_list[8]['time']
    content9 = weibo_list[8]['text']
    id10 = weibo_list[9]['author_uid']
    author10 = weibo_list[9]['author_name']
    location10 = weibo_list[9]['location']
    time10 = weibo_list[9]['time']
    content10 = weibo_list[9]['text']
    id11 = weibo_list[10]['author_uid']
    author11 = weibo_list[10]['author_name']
    location11 = weibo_list[10]['location']
    time11 = weibo_list[10]['time']
    content11 = weibo_list[10]['text']
    id12 = weibo_list[11]['author_uid']
    author12 = weibo_list[11]['author_name']
    location12 = weibo_list[11]['location']
    time12 = weibo_list[11]['time']
    content12 = weibo_list[11]['text']

    return render(request, 'Real-time_monitor.html',{'List1':json.dumps(List1),'List2':json.dumps(List2),
                                                     'id1':json.dumps(id1),
                                                     'author1':json.dumps(author1),
                                                     'location1':json.dumps(location1),
                                                     'time1':json.dumps(time1),
                                                     'content1':json.dumps(content1),
                                                     'id2':json.dumps(id2),
                                                     'author2':json.dumps(author2),
                                                     'location2':json.dumps(location2),
                                                     'time2':json.dumps(time2),
                                                     'content2':json.dumps(content2),
                                                        'id3':json.dumps(id3),
                                                     'author3':json.dumps(author3),
                                                     'location3':json.dumps(location3),
                                                     'time3':json.dumps(time3),
                                                     'content3':json.dumps(content3),
                                                     'id4':json.dumps(id4),
                                                     'author4':json.dumps(author4),
                                                     'location4':json.dumps(location4),
                                                     'time4':json.dumps(time4),
                                                     'content4':json.dumps(content4),
                                                     'id5': json.dumps(id5),
                                                     'author5': json.dumps(author5),
                                                     'location5': json.dumps(location5),
                                                     'time5': json.dumps(time5),
                                                     'content5': json.dumps(content5),
                                                     'id6': json.dumps(id6),
                                                     'author6': json.dumps(author6),
                                                     'location6': json.dumps(location6),
                                                     'time6': json.dumps(time6),
                                                     'content6': json.dumps(content6),
                                                     'id7': json.dumps(id7),
                                                     'author7': json.dumps(author7),
                                                     'location7': json.dumps(location7),
                                                     'time7': json.dumps(time7),
                                                     'content7': json.dumps(content7),
                                                     'id8': json.dumps(id8),
                                                     'author8': json.dumps(author8),
                                                     'location8': json.dumps(location8),
                                                     'time8': json.dumps(time8),
                                                     'content8': json.dumps(content8),
                                                     'id9': json.dumps(id9),
                                                     'author9': json.dumps(author9),
                                                     'location9': json.dumps(location9),
                                                     'time9': json.dumps(time9),
                                                     'content9': json.dumps(content9),
                                                     'id10': json.dumps(id10),
                                                     'author10': json.dumps(author10),
                                                     'location10': json.dumps(location10),
                                                     'time10': json.dumps(time10),
                                                     'content10': json.dumps(content10),
                                                     'id11': json.dumps(id11),
                                                     'author11': json.dumps(author11),
                                                     'location11': json.dumps(location11),
                                                     'time11': json.dumps(time11),
                                                     'content11': json.dumps(content11),
                                                     'id12': json.dumps(id12),
                                                     'author12': json.dumps(author12),
                                                     'location12': json.dumps(location12),
                                                     'time12': json.dumps(time12),
                                                     'content12': json.dumps(content12)

                                                     })  #只返回html  其他的实时数据从data1中获取


def weibo_data(request):    #微博数据页面

    weibo_all = realtime_object_1.get_all_weibo_from_mongodb()
    List5 = []
    for weibo in weibo_all:
        List5.append(
                {
                    "user_id": weibo['author_uid'],
                    "user_author": weibo['author_name'],
                    "user_location": weibo['location'],
                    "user_time": weibo['time'],
                    "user_content": weibo['text']
                }
        )
    weibo_threaten = realtime_object_1.get_all_threaten_weibo_from_mongodb()
    weibo_threaten_2 = realtime_object_1.get_temp_threaten_relationship_from_mongodb()
    len_threaten = len(weibo_threaten)
    while len_threaten < 5:
        weibo_threaten.append(
            {
                "author_uid": ' ',
                "author_name": ' ',
                "location": ' ',
                "time": ' ',
                "text": ' ',
            }
        )
        len_threaten += 1

    # List5 = [{"user_id": "2919565921", "user_author": "好善乐施", "user_location": "烟台", "user_time": "2017-05-27 16:36:30",
    #   "user_content": "好久没有更博了，就发张过敏PS的照片吧[二哈]"},
    #  {"user_id": "2113930241", "user_author": "无懈可击", "user_location": "潍坊", "user_time": "2017-05-27 16:31:49",
    #   "user_content": "我围观了@唯我落日 的回答，该问题价值50.00元，围观仅1元，快来一起围观~ http://t.cn/RiJMXJr"}]       #微博数据分析  列表里的数据
    id1=weibo_threaten[0]['author_uid']
    #敏感微博的 id author location time content  共5个
    author1=weibo_threaten[0]['author_name']
    location1=weibo_threaten[0]['location']
    time1=weibo_threaten[0]['time']
    content1=weibo_threaten[0]['text']
    id2=weibo_threaten[1]['author_uid']
    author2=weibo_threaten[1]['author_name']
    location2=weibo_threaten[1]['location']
    time2=weibo_threaten[1]['time']
    content2=weibo_threaten[1]['text']
    id3=weibo_threaten[2]['author_uid']
    author3=weibo_threaten[2]['author_name']
    location3=weibo_threaten[2]['location']
    time3=weibo_threaten[2]['time']
    content3=weibo_threaten[2]['text']
    id4=weibo_threaten[3]['author_uid']
    author4=weibo_threaten[3]['author_name']
    location4=weibo_threaten[3]['location']
    time4=weibo_threaten[3]['time']
    content4=weibo_threaten[3]['text']
    id5=weibo_threaten[4]['author_uid']
    author5=weibo_threaten[4]['author_name']
    location5=weibo_threaten[4]['location']
    time5=weibo_threaten[4]['time']
    content5=weibo_threaten[4]['text']
    # List1-List4 是关系图的参数
    List1 = []
    List2 = []
    List3 = []
    count = -1
    for weibo in weibo_threaten_2:
        count += 1
        List1.append(
            {
                "name": weibo['name'],
                "keyword": {},
                "base": weibo['name']
            }
        )
        List2.append(
            {
                "name": weibo['name'],
                "value": 10,
                "category": count
            }
        )
        for fans in weibo['fans_list']:
            List2.append(
                {
                    "name": fans['name'],
                    "value": 20,
                    "category": count
                }
            )
    count_1 = 0
    start_num = 0
    for i in range(count+2):
        for person in List2:
            if person['category'] == i:
                List3.append(
                    {
                        "source": start_num,
                        "target": start_num+count_1
                    }
                )
                count_1 += 1
        start_num = start_num+count_1
        count_1 = 0

    List4 = []
    for person in weibo_threaten_2:
        List4.append(person['name'])

    provice_id_list = [16, 15, 14, 9, 12, 19, 27, 10, 25, 30, 1, 2, 7]
    list22 = []
    for id in provice_id_list:
        weibo_list = realtime_object_1.get_target_province_weibo(id)
        id_num = len(weibo_list)
        list22.append(id_num)
    list33 = []
    for id in provice_id_list:
        weibo_list = realtime_object_1.get_target_province_threaten_weibo(id)
        id_num = len(weibo_list)
        list33.append(id_num)

    list22_max_value = max(list22)
    for index, id_num in enumerate(list22):
        if id_num == list22_max_value:
            list22_max_index = provice_id_list[index]
            break

    list22_min_value = min(list22)
    for index, id_num in enumerate(list22):
        if id_num == list22_min_value:
            list22_min_index = provice_id_list[index]
            break
    # List11-List44 是微博柱状图
    List11 =  ['山西','山东','河南','河北','陕西', '江苏','广东','新疆','浙江','台湾','北京','上海', '辽宁']   #横坐标 为地区
    List22 = list22            #红色 微博量的数值
    List33 = list33              #灰色 敏感量的数值
    List44 = [  {'name' : '最高', 'value' : list22_max_value, 'xAxis': list22_max_index, 'yAxis': list22_max_value},                    #柱状图的最高最低的 横坐标 纵坐标
                    {'name ': '最低', 'value' : list22_min_value, 'xAxis': list22_min_index, 'yAxis': list22_min_value}]


    return render(request, 'weibo_data.html',{ 'List5':json.dumps(List5),
        'id1':json.dumps(id1),
        'author1':json.dumps(author1),
        'location1':json.dumps(location1),
        'time1':json.dumps(time1),
        'content1':json.dumps(content1),
       'id2': json.dumps(id2),
       'author2': json.dumps(author2),
       'location2': json.dumps(location2),
       'time2': json.dumps(time2),
       'content2': json.dumps(content2),
       'id3': json.dumps(id3),
       'author3': json.dumps(author3),
       'location3': json.dumps(location3),
       'time3': json.dumps(time3),
       'content3': json.dumps(content3),
       'id4': json.dumps(id4),
       'author4': json.dumps(author4),
       'location4': json.dumps(location4),
       'time4': json.dumps(time4),
       'content4': json.dumps(content4),
       'id5': json.dumps(id5),
       'author5': json.dumps(author5),
       'location5': json.dumps(location5),
       'time5': json.dumps(time5),
       'content5': json.dumps(content5),

        'List1': json.dumps(List1),
        'List2': json.dumps(List2),
        'List3': json.dumps(List3),
        'List4': json.dumps(List4),

       'List11': json.dumps(List11),
       'List22': json.dumps(List22),
       'List33': json.dumps(List33),
       'List44': json.dumps(List44),

                                               })



def zhihu_data(request):
    id1 = 1
    tittle1 = "二本学校的学生想考研到211、985学校现实吗？"
    p1 = 0.00280787122047
    answer_words1 = '"考研" "学校" "专业课" "专业" "自己" "二本" "985" "211" "真题" "同学" "复试" "这个"'
    id2 = 2
    tittle2 = "211、985的学生们是怎么看待三本、专科的学生们的?"
    p2 = 0.00331893793986
    answer_words2 = '"985" "211" "学校" "三本" "高中" "二本" "这个" "我们" "标签" "觉得" "学生" "同学"'
    id3 = 3
    tittle3 = "211 的本科生和专科生有可能在一起吗？"
    p3 = 0.00287639710717
    answer_words3 = '"211" "专科生" "三观" "......" "985" "学历" "一个" "妹纸" "感情" "是否" "合适" "题主"'
    id4 = 4
    tittle4 = "985、211、双非一本、二本A、二本B（三本）、专A、专B的差别、差距到底在哪里?"
    p4 = 0.00419185377087
    answer_words4 = '"985" "学校" "211" "本科" "时候" "二本" "图书馆" "考研" "自己" "一样" "我们" "就是"'
    id5 = 5
    tittle5 = "清华本科+211硕士，211本科+清华硕士，哪个人的就业更胜一筹？"
    p5 = 0.16165413533834577
    answer_words5 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
    id6 = 6
    tittle6 = "李文富哦好"
    p6 = 0.00447949059677
    answer_words6 = '"本科" "清北" "硕士" "211" "高晓松" "清华" "学历" "出身" "一个" "博士" "985" "公平"'
    id7 = 7
    tittle7 = "李文富哦好"
    p7 = 0.16165413533834577
    answer_words7 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
    id8 = 8

    tittle8 = "985、211 高校毕业的电气硕士，去国家电网合适吗？"
    p8 =0.00365106504239
    answer_words8 = '"国网" "电网" "同学" "甘心" "自己" "行业" "科研" "国企" "工作" "进入" "选择" "毕业"'
    List5 = [
        {"user_id": "2919565921", "user_author": "-Liu爱秋", "user_location": "烟台", "user_time": "2017-05-27 16:36:30",
         "user_content": "好久没有更博了，就发张过敏PS的照片吧[二哈]"},
        {"user_id": "2113930241", "user_author": "旷野星辰188", "user_location": "潍坊", "user_time": "2017-05-27 16:31:49",
         "user_content": "我围观了@唯我落日 的回答，该问题价值50.00元，围观仅1元，快来一起围观~ http://t.cn/RiJMXJr"}]  # 知乎回答内容

    leaderid1 = 1;
    leader1 = "法国培根";
    address1 = "旅日华人，前职咨询，现创业公司。参与过日本零售、金融、IT等行业项目。主要答题范围：日语/日本政经社/电子产品/设计/东京生活";
    leaderid2 = 2;
    leader2 = "张小凡";
    address2 = "数码科技摄影爱好者&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    leaderid3 = 3;
    leader3 = "阿肥";
    address3 = "现居深圳/计算机软件/勇气和梦想永不褪色";
    leaderid4 = 4;
    leader4 = "楊甚麽";
    address4 = "知乎电气QQ群：397942911/我已委托“维权骑士”（http://rightknights.com）为我的文章进行维权";
    leaderid5 = 5;
    leader5 = "喜欢就叨几句";
    address5 = "回不回答，全凭心情。就是任性！&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    leaderid6 = 6;
    leader6 = "秋月酱";
    address6 = "私募/操盘私募&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    leaderid7 = 7;
    leader7 = "逸叔";
    address7 = "闪存内存工程师，空手道黑带，什么都感兴趣一点~";
    leaderid8 = 8;
    leader8 = "苏星";
    address8 = "图钉/woter卡基/图钉/woter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";

    List1 = ['rose1', 'rose2', 'rose3', 'rose4', 'rose5', 'rose6', 'rose7', 'rose8'
             ]
    List2 = [{'value': 10, 'name': 'rose1'},
             {'value': 5, 'name': 'rose2'},
             {'value': 15, 'name': 'rose3'},
             {'value': 25, 'name': 'rose4'},
             {'value': 20, 'name': 'rose5'},
             {'value': 35, 'name': 'rose6'},
             {'value': 30, 'name': 'rose7'},
             {'value': 40, 'name': 'rose8'}]

    return render(request, 'zhihu_data.html', {
        'leader1': json.dumps(leader1),
        'address1': json.dumps(address1),
        'leader2': json.dumps(leader2),
        'address2': json.dumps(address2),
        'leader3': json.dumps(leader3),
        'address3': json.dumps(address3),
        'leader4': json.dumps(leader4),
        'address4': json.dumps(address4),
        'leader5': json.dumps(leader5),
        'address5': json.dumps(address5),
        'leader6': json.dumps(leader6),
        'address6': json.dumps(address6),
        'leader7': json.dumps(leader7),
        'address7': json.dumps(address7),
        'leader8': json.dumps(leader8),
        'address8': json.dumps(address8),
        'leaderid1': json.dumps(leaderid1),
        'leaderid2': json.dumps(leaderid2),
        'leaderid3': json.dumps(leaderid3),
        'leaderid4': json.dumps(leaderid4),
        'leaderid5': json.dumps(leaderid5),
        'leaderid6': json.dumps(leaderid6),
        'leaderid7': json.dumps(leaderid7),
        'leaderid8': json.dumps(leaderid8),
        'List5': json.dumps(List5),
		'id1':json.dumps(id1),
		'id2':json.dumps(id2),
		'id3':json.dumps(id3),
		'id4':json.dumps(id4),
		'id5':json.dumps(id5),
		'id6':json.dumps(id6),
		'id7':json.dumps(id7),
		'id8':json.dumps(id8),
        'tittle1': json.dumps(tittle1),
        'p1': json.dumps(p1),
        'answer_words1': json.dumps(answer_words1),
        'tittle2': json.dumps(tittle2),
        'p2': json.dumps(p2),
        'answer_words2': json.dumps(answer_words2),
        'tittle3': json.dumps(tittle3),
        'p3': json.dumps(p3),
        'answer_words3': json.dumps(answer_words3),
        'tittle4': json.dumps(tittle4),
        'p4': json.dumps(p4),
        'answer_words4': json.dumps(answer_words4),
        'tittle5': json.dumps(tittle5),
        'p5': json.dumps(p5),
        'answer_words5': json.dumps(answer_words5),
        'tittle6': json.dumps(tittle6),
        'p6': json.dumps(p6),
        'answer_words6': json.dumps(answer_words6),
        'tittle7': json.dumps(tittle7),
        'p7': json.dumps(p7),
        'answer_words7': json.dumps(answer_words7),
        'tittle8': json.dumps(tittle8),
        'p8': json.dumps(p8),
        'answer_words8': json.dumps(answer_words8),
        'List1': json.dumps(List1),
        'List2': json.dumps(List2),
    })


def data_pic(request):  #数据图片分析页
    return render(request, 'data_pic.html')

def provice_weibo_data(request,a):    #每个地区的微博信息
    #地区微博数据  5条的id  author location time content
    print  'provice is '+a
    a=int(a)
    if a == 1:
        province = '北京市微博数据'
    elif a == 2:
        province = '上海市微博数据'
    elif a == 3:
        province = '天津市微博数据'
    elif a == 4:
        province = '重庆市微博数据'
    elif a == 5:
        province = '黑龙江省微博数据'
    elif a == 6:
        province = '吉林省微博数据'
    elif a == 7:
        province = '辽宁省微博数据'
    elif a == 8:
        province = '内蒙古微博数据'
    elif a == 9:
        province = '河北省微博数据'
    elif a == 10:
        province = '新疆省微博数据'
    elif a == 11:
        province = '甘肃省微博数据'
    elif a == 12:
        province = '陕西省微博数据'
    elif a == 13:
        province = '宁夏省微博数据'
    elif a == 14:
        province = '河南省微博数据'
    elif a == 15:
        province = '山东省微博数据'
    elif a == 16:
        province = '山西省微博数据'
    elif a == 17:
        province = '安徽省微博数据'
    elif a == 18:
        province = '湖北省微博数据'
    elif a == 19:
        province = '江苏省微博数据'
    elif a == 20:
        province = '四川省微博数据'
    elif a == 21:
        province = '贵州省微博数据'
    elif a == 22:
        province = '云南省微博数据'
    elif a == 23:
        province = '广西省微博数据'
    elif a == 24:
        province = '西藏省微博数据'
    elif a == 25:
        province = '浙江省微博数据'
    elif a == 26:
        province = '江西省微博数据'
    elif a == 27:
        province = '广东省微博数据'
    elif a == 28:
        province = '福建省微博数据'
    elif a == 29:
        province = '海南省微博数据'
    elif a == 30:
        province = '台湾省微博数据'
    elif a == 31:
        province = '贵州省微博数据'
    elif a == 32:
        province = '青海省微博数据'
    elif a == 33:
        province = '湖南省微博数据'

    List1 = []
    weibo_list = realtime_object_1.get_target_province_weibo(a)
    for weibo in weibo_list:
        List1.append(
            {
                "user_id": weibo['uid'],
                "user_author": weibo['author_name'],
                "user_location": weibo['location'],
                "user_time": weibo['time'],
                "user_content": weibo['text'],
            }
        )
    #
    # List1 = [{"user_id":"2919565921","user_author":"-Liu爱秋","user_location":"烟台","user_time":"2017-05-27 16:36:30","user_content":"好久没有更博了，就发张过敏PS的照片吧[二哈]"},
    #          {"user_id":"2113930241","user_author":"旷野星辰188","user_location":"潍坊","user_time":"2017-05-27 16:31:49","user_content":"我围观了@唯我落日 的回答，该问题价值50.00元，围观仅1元，快来一起围观~ http://t.cn/RiJMXJr"}]

    return render(request, 'provice_weibo_data.html',{
        'List1':json.dumps(List1),
        'province':json.dumps(province),
    })

def data1(request):  #实时监测地图的数据来源

        # count 是要获取的微博数量
        count = 10
        weibo_list = [{'location':'上海','repost_location':'北京','threatened':56,'is_repost':1,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      {'location': '西安', 'repost_location': '上海', 'threatened': 77, 'is_repost': 1,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      {'location': '温州', 'repost_location': '北京', 'threatened': 45, 'is_repost': 1,'id':'46789','author':'体育局培根','time':'2017.5','content':'微博内容和'},
                      {'location': '杭州', 'repost_location': '杭州', 'threatened': 65, 'is_repost': 0,'id':'46789','author':'法不二越根','time':'2017.5','content':'微博内容和'},
                      {'location': '上海', 'repost_location': '上海', 'threatened': 25, 'is_repost': 0,'id':'46789','author':'二哥','time':'2017.5','content':'微博内容和'},
                      {'location': '上海', 'repost_location': '北京', 'threatened': 89, 'is_repost': 1,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      {'location': '常州', 'repost_location': '深圳', 'threatened': 12, 'is_repost': 1,'id':'46789','author':'法国王伟培根','time':'2017.5','content':'微博内容和'},
                      {'location': '深圳', 'repost_location': '武汉', 'threatened': 45, 'is_repost': 0,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      {'location': '上海', 'repost_location': '西安', 'threatened': 47, 'is_repost': 1,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      {'location': '北京', 'repost_location': '北京', 'threatened': 35, 'is_repost': 0,'id':'46789','author':'法国培根','time':'2017.5','content':'微博内容和'},
                      ]



        print weibo_list
        # weiboinfo_list = start_run()  #返回列表 里面是字典
        rjson = json.dumps(weibo_list)
        response = HttpResponse()
        response['Content-Type'] = "text/javascript"
        response.write(rjson)
        return response


def data2(request):
    List2 = [{'name':'上海','value':95},
             {'name':'广州','value':90},
             {'name':'大连','value':80},
             {'name':'南宁','value':70},
             {'name':'南昌','value':60},
             {'name':'拉萨','value':50},
             {'name':'长春','value':40},
             {'name':'包头','value':30},
             {'name':'重庆','value':20},
             {'name':'常州','value':10}]
    print 'r2'
    print List2
    return JsonResponse(List2, safe=False)


def login(request):
    return render(request, 'login.html')

def search(request, a):
    print "a is " + a

    zhihumongo_object_1.start_run(a)
    top_list = zhihumongo_object_1.get_top_people_from_mongodb()
    for people in top_list:
        if not people.has_key('description'):
            people['description'] = '暂无'
    flag = zhihumongo_object_1.start_run(a)
    if flag != 1:
        leaderid1 = '1'
        leaderid2 = '1'
        leaderid3 = '1'
        leaderid4 = '1'
        leaderid5 = '1'
        leaderid6 = '1'
        leaderid7 = '1'
        leaderid8 = '1'
        leader1 = "正在分析。。"
        leader2 = "正在分析。。"
        leader3 = "正在分析。。"
        leader4 = "正在分析。。"
        leader5 = "正在分析。。"
        leader6 = "正在分析。。"
        leader7 = "正在分析。。"
        leader8 = "正在分析。。"

        address1 = "正在分析。。"
        address2 = "正在分析。。"
        address3 = "正在分析。。"
        address4 = "正在分析。。"
        address5 = "正在分析。。"
        address6 = "正在分析。。"
        address7 = "正在分析。。"
        address8 = "正在分析。。"
        id1 = '0'
        id2 = '0'
        id3 = '0'
        id4 = '0'
        id5 = '0'
        id6 = '0'
        id7 = '0'
        id8 = '0'

        List5 = [{"user_id": "2919565921", "user_author": "-射雕v鼠标算法泊松分布爱秋", "user_location": "烟台",
                  "user_time": "2017-05-27 16:36:30", "user_content": "好久没有更博了，就发张过敏PS的照片吧[二哈]"},
                 {"user_id": "2113930241", "user_author": "旷野星辰188", "user_location": "潍坊",
                  "user_time": "2017-05-27 16:31:49",
                  "user_content": "我围观了@唯我落日 的回答，该问题价值50.00元，围观仅1元，快来一起围观~ http://t.cn/RiJMXJr"}]

        tittle1 = '额风格'
        p1 = 0.16165413533834577
        answer_words1 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle2 = "李文富哦好"
        p2 = 0.16165413533834577
        answer_words2 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle3 = "李文富哦好"
        p3 = 0.16165413533834577
        answer_words3 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle4 = "李文富哦好"
        p4 = 0.16165413533834577
        answer_words4 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle5 = "李文富哦好"
        p5 = 0.16165413533834577
        answer_words5 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle6 = "李文富哦好"
        p6 = 0.16165413533834577
        answer_words6 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle7 = "李文富哦好"
        p7 = 0.16165413533834577
        answer_words7 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""
        tittle8 = "李文富哦好"
        p8 = 0.16165413533834577
        answer_words8 = "\"三星\",\"手机\",\"现在\",\"质量\",\"觉得\",\"之后\",\"推荐\",\"然后\",\"用户\",\"出来\",\"充电\",\"时候\",\"什么\""


    else:

        leaderid1 = top_list[0]['id']
        leaderid2 = top_list[1]['id']
        leaderid3 = top_list[2]['id']
        leaderid4 = top_list[3]['id']
        leaderid5 = top_list[4]['id']
        leaderid6 = top_list[5]['id']
        leaderid7 = top_list[6]['id']
        leaderid8 = top_list[7]['id']
        leader1=top_list[0]['name']        #知乎领袖意见   中的 昵称 和  address   共8个
        address1=top_list[0]['description']
        leader2=top_list[1]['name']
        address2=top_list[1]['description']
        leader3=top_list[2]['name']
        address3=top_list[2]['description']
        leader4=top_list[3]['name']
        address4=top_list[3]['description']
        leader5=top_list[4]['name']
        address5=top_list[4]['description']
        leader6=top_list[5]['name']
        address6=top_list[5]['description']
        leader7=top_list[6]['name']
        address7=top_list[6]['description']
        leader8=top_list[7]['name']
        address8=top_list[7]['description']
        List5 = []
        for person in zhihumongo_object_1.get_all_people_from_mongodb():
            List5.append(
                {
                    "user_id": person['id'],
                    "user_author": person['name'],
                    "location": person['this_answer_question_id'],
                    "user_time": person['voteup_count'],
                    "user_content": person['this_answer_content'][:30]
                }
            )

        question_list = get_high_frequency_vocabulary(a)
        len_question_list = len(question_list)
        if len_question_list < 8:
            for i in range(8-len_question_list):
                question_list.append(
                    {
                        "frequency": 0,
                        "words_list": [],
                        "question_id": '0',
                        "question_title": '暂无',
                    }
                )
        id1 = question_list[0]["question_id"]
        id2 = question_list[1]["question_id"]
        id3 = question_list[2]["question_id"]
        id4 = question_list[3]["question_id"]
        id5 = question_list[4]["question_id"]
        id6 = question_list[5]["question_id"]
        id7 = question_list[6]["question_id"]
        id8 = question_list[7]["question_id"]
        tittle1 = question_list[0]["question_title"]
        tittle2 = question_list[1]["question_title"]
        tittle3 = question_list[2]["question_title"]
        tittle4 = question_list[3]["question_title"]
        tittle5 = question_list[4]["question_title"]
        tittle6 = question_list[5]["question_title"]
        tittle7 = question_list[6]["question_title"]
        tittle8 = question_list[7]["question_title"]
        p1 = str(question_list[0]['frequency'])
        p2 = str(question_list[1]['frequency'])
        p3 = str(question_list[2]['frequency'])
        p4 = str(question_list[3]['frequency'])
        p5 = str(question_list[4]['frequency'])
        p6 = str(question_list[5]['frequency'])
        p7 = str(question_list[6]['frequency'])
        p8 = str(question_list[7]['frequency'])

        word_str = ''
        for word in question_list[0]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words1 = word_str

        word_str = ''
        for word in question_list[1]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words2 = word_str

        word_str = ''
        for word in question_list[2]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words3 = word_str

        word_str = ''
        for word in question_list[3]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words4 = word_str

        word_str = ''
        for word in question_list[4]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words5 = word_str

        word_str = ''
        for word in question_list[5]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words6 = word_str

        word_str = ''
        for word in question_list[6]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words7 = word_str

        word_str = ''
        for word in question_list[7]["words_list"]:
            word_str = word_str + ' "'+word + '" '
        answer_words8 = word_str

        List5 = []
        for person in zhihumongo_object_1.get_all_people_from_mongodb():
            List5.append(
                {
                    "user_id": person['id'],
                    "user_author": person['name'],
                    "location": person['location'],
                    "user_time": person['this_answer_question_id'],
                    "user_content": person['this_answer_content'][:30]
                }
            )

    print(leader1, address1)
    print leader2, leader3, leader4

    zhihumongo_object_1.get_ciyun1("business")
    zhihumongo_object_1.get_ciyun1("location")
    zhihumongo_object_1.get_ciyun1("question")

    b_v_list = zhihumongo_object_1.get_business_and_value_from_mongodb()
    List1 = []
    List2 = []
    for b_v_dict in b_v_list:
        List1.append(b_v_dict["name"])
        List2.append(b_v_dict)

    return render(request, 'zhihu_data.html', {
        'leader1': json.dumps(leader1),
        'address1': json.dumps(address1),
        'leader2': json.dumps(leader2),
        'address2': json.dumps(address2),
        'leader3': json.dumps(leader3),
        'address3': json.dumps(address3),
        'leader4': json.dumps(leader4),
        'address4': json.dumps(address4),
        'leader5': json.dumps(leader5),
        'address5': json.dumps(address5),
        'leader6': json.dumps(leader6),
        'address6': json.dumps(address6),
        'leader7': json.dumps(leader7),
        'address7': json.dumps(address7),
        'leader8': json.dumps(leader8),
        'address8': json.dumps(address8),
        'leaderid1': json.dumps(leaderid1),
        'leaderid2': json.dumps(leaderid2),
        'leaderid3': json.dumps(leaderid3),
        'leaderid4': json.dumps(leaderid4),
        'leaderid5': json.dumps(leaderid5),
        'leaderid6': json.dumps(leaderid6),
        'leaderid7': json.dumps(leaderid7),
        'leaderid8': json.dumps(leaderid8),
        'List5': json.dumps(List5),
        'id1': json.dumps(id1),
        'id2': json.dumps(id2),
        'id3': json.dumps(id3),
        'id4': json.dumps(id4),
        'id5': json.dumps(id5),
        'id6': json.dumps(id6),
        'id7': json.dumps(id7),
        'id8': json.dumps(id8),
        'tittle1': json.dumps(tittle1),
        'p1': json.dumps(p1),
        'answer_words1': json.dumps(answer_words1),
        'tittle2': json.dumps(tittle2),
        'p2': json.dumps(p2),
        'answer_words2': json.dumps(answer_words2),
        'tittle3': json.dumps(tittle3),
        'p3': json.dumps(p3),
        'answer_words3': json.dumps(answer_words3),
        'tittle4': json.dumps(tittle4),
        'p4': json.dumps(p4),
        'answer_words4': json.dumps(answer_words4),
        'tittle5': json.dumps(tittle5),
        'p5': json.dumps(p5),
        'answer_words5': json.dumps(answer_words5),
        'tittle6': json.dumps(tittle6),
        'p6': json.dumps(p6),
        'answer_words6': json.dumps(answer_words6),
        'tittle7': json.dumps(tittle7),
        'p7': json.dumps(p7),
        'answer_words7': json.dumps(answer_words7),
        'tittle8': json.dumps(tittle8),
        'p8': json.dumps(p8),
        'answer_words8': json.dumps(answer_words8),
        'List1': json.dumps(List1),
        'List2': json.dumps(List2),
    })


if __name__ == '__main__':
    print("54")