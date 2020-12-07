# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:29:36 2020

@author: User
"""

import requests
import re
import pandas as pd
import time
import math
 
def queryLongitude(addr):
    #查询addr的经纬度
    template = 'https://apis.map.qq.com/jsapi?qt=geoc&addr={addr}&key=UGMBZ-CINWR-DDRW5-W52AK-D3ENK-ZEBRC&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb2.geocoder0'
    url = template.format(addr=addr)
    resp = requests.get(url)
    x = re.findall('pointx":"(.*?)",',resp.text)[0]
    return x
def queryLatitude(addr):
    #查询addr的经纬度
    template = 'https://apis.map.qq.com/jsapi?qt=geoc&addr={addr}&key=UGMBZ-CINWR-DDRW5-W52AK-D3ENK-ZEBRC&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb2.geocoder0'
    url = template.format(addr=addr)
    resp = requests.get(url)
    y = re.findall('pointy":"(.*?)",',resp.text)[0]
    return y
def main():
    #文件名称
    fileName="test.csv"
    df=pd.read_csv(fileName,encoding="gbk")
    #关闭警告
    pd.set_option('mode.chained_assignment', None)
    # 每次处理的个数,爬虫无法同一时间爬取大量信息，需要分别进行查询，默认十秒爬取25个
    size=25
    # （秒）
    sleepTime=10
    df['经度']=None
    df['纬度']=None
    df.to_csv(fileName, encoding="gbk",index=None)
    for i in range(0,df['addr'].size,size):
        print(str(int(i/size+1))+"/"+str(math.ceil(df['addr'].size/size)))
        dftemp=df[i:i+size]
        try:
            df1=dftemp['addr'].apply(queryLongitude)
            df2=dftemp['addr'].apply(queryLatitude)
            df['经度'][i:i+size]=df1
            df['纬度'][i:i+size]=df2
        except:
            upper=(i+size) if (i+size)<df['addr'].size else df['addr'].size
            for j in range(i,upper):
                try:
                    longitude=queryLongitude(df['addr'][j])
                    df['经度'][j]=longitude
                    latitude=queryLatitude(df['addr'][j])
                    df['纬度'][j]=latitude
                except:
                    print("无法解析地址："+df['addr'][j])                    
        time.sleep(sleepTime)
    df.to_csv(fileName, encoding="gbk",index=None) 
    print("生成经纬度完成")
if __name__=='__main__':
    main()