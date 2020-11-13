# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:29:36 2020

@author: User
"""

import requests
import re
import pandas as pd
 
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
    fileName=input("请输入文件名：")
    if fileName=="":
        fileName="test.CSV"
    df=pd.read_csv(fileName,encoding="gbk")
    df['经度']=df['addr'].apply(queryLongitude)
    df['纬度']=df['addr'].apply(queryLatitude)
    df.to_csv(fileName, encoding="gbk",index=None) 
if __name__=='__main__':
    main()