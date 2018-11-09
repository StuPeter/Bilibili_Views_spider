#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/10/30
# @Author  : 圈圈烃
# @File    : bili_online_analysis
# @Description: B站在线数据获取
#
#
from BiliSpider import BiliSpider
from pymongo import MongoClient
import datetime


def online_info(bili, online_info_db, timestamp):
    """
    保存在线信息
    :param bili: 类
    :param online_info_db: 数据库
    :param timestamp: 时间戳
    :return:
    """
    online_dic = bili.get_online()
    all_count = online_dic['data']['all_count']     # 最新投稿
    web_online = online_dic['data']['web_online']    # 在线人数
    data_dic = {
        "时间戳": timestamp,
        "最新投稿": all_count,
        "在线人数": web_online,
    }
    # 存入数据库
    online_info_db.insert_one(data_dic)
    print("数据保存成功... %s" % timestamp)


def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # 连接数据库
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.bili_db
    online_info_db = db.online_info
    # 创建爬虫
    bili = BiliSpider()
    online_info(bili, online_info_db, timestamp)


if __name__ == '__main__':
    main()