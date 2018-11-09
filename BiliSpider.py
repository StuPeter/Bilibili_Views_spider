#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/10/25
# @Author  : 圈圈烃
# @File    : BiliSpider
# @Description:
#
#
import requests
import json


class BiliSpider:
    def __init__(self):
        self.online_api = "https://api.bilibili.com/x/web-interface/online"  # 在线人数
        self.video_api = "https://api.bilibili.com/x/web-interface/archive/stat?&aid=%s"    # 视频信息
        self.newlist_api = "https://api.bilibili.com/x/web-interface/newlist?&rid=%s&pn=%s&ps=%s"     # 最新视频信息
        self.region_api = "https://api.bilibili.com/x/web-interface/dynamic/region?&rid=%s&pn=%s&ps=%s"  # 最新动态信息
        self.member_api = "http://space.bilibili.com/ajax/member/GetInfo"  # 用户信息
        self.stat_api = "https://api.bilibili.com/x/relation/stat?vmid=%s"  # 用户关注数和粉丝总数
        self.upstat_api = "https://api.bilibili.com/x/space/upstat?mid=%s"     # 用户总播放量和总阅读量
        self.follower_api = "https://api.bilibili.com/x/relation/followings?vmid=%s&pn=%s&ps=%s"    # 用户关注信息
        self.fans_api = "https://api.bilibili.com/x/relation/followers?vmid=%s&pn=%s&ps=%s"    # 用户粉丝信息

    def get_api(api_url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Host": "api.bilibili.com",
            "Referer": "https://www.bilibili.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        }
        res = requests.get(api_url, headers=headers)
        res_dict = res.json()
        return res_dict

    def get_online(self):
        """
        获取在线信息
        all_count: 最新投稿
        web_online: 在线人数
        :return:
        """
        online_dic = BiliSpider.get_api(self.online_api)
        return online_dic

    def get_video_info(self, aid):
        """
        获取视频信息
        :param aid: 视频id
        :return:
        """
        res = BiliSpider.get_api(self.video_api %aid)
        # print(res)
        return res

    def get_newlist_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.newlist_api %(rid, pn, ps))
        return res

    def get_region_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.region_api %(rid, pn, ps))
        return res

    def get_member_info(self, mid):
        """
        获取用户信息
        :param mid:用户id
        :return:
        """
        post_data = {
            "crsf": "",
            "mid": mid,
        }
        header = {
            "Host": "space.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Referer": "https://www.bilibili.com/",
        }
        res = requests.post(self.member_api, data=post_data, headers=header)
        member_dic = json.dumps(res.json(), ensure_ascii=False)
        return member_dic

    def get_stat_info(self, vmid):
        """
        获取某用户的关注数和粉丝总数
        :param vmid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.stat_api % vmid)
        return res

    def get_upstat_info(self, mid):
        """
        获取某用户的总播放量和总阅读量
        :param mid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.upstat_api % mid)
        return res

    def get_follower_info(self, vmid, pn, ps):
        """
        获取某用户关注者信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.follower_api %(vmid, pn, ps))
        return res

    def get_fans_info(self, vmid, pn, ps):
        """
        获取某用户粉丝信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.fans_api %(vmid, pn, ps))
        return res


if __name__ == '__main__':
    bili = BiliSpider()
    res = bili.get_member_info("330626607")
    print(res)

