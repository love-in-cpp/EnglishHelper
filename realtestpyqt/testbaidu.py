# -*- coding = utf-8 -*-
# @Time : 2021/7/5 16:32
# @Author : 刘正阳
# @File : testbaidu.py
# @Software : PyCharm


import http.client
import hashlib
import urllib
import random
import json
from pip._vendor.distlib.compat import raw_input

# 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
appid = '20210705000880494'  # 填写你的appid
secretKey = 'N8Ulz_0geVaxzpDoBbb7'  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

fromLang = 'auto'  # 原文语种
toLang = 'zh'  # 译文语种
salt = random.randint(32768, 65536)
# 手动录入翻译内容，q存放
#q = raw_input("please input the word you want to translate:")
q = 'baby'
sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
        '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

# 建立会话，返回结果
try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    r_result = result['trans_result'][0]
    print(r_result['dst'])

except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
