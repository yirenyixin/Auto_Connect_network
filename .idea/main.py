# _*_ coding : utf-8 _*_

import re    # 正则表达式，用于匹配字符
from urllib import request

import chardet as chardet
import requests    # 用于向目标网站发送请求
import time

#url = 'http://10.23.2.4/eportal/index.jsp?wlanuserip=1d90ec446c6b52bb80a013e0ee83ccd2&wlanacname=eb3dea19c415ccae600bdc9db5d15bde&ssid=512b4fa22cd47690c1d677b390465049&nasip=390c1cf6eea7dfbca3f3f0aca4b4d442&mac=20617c667d26c7015c5889cba8afcce5&t=wireless-v2&url=4be2aa94e61657a37b1da9b0c8748ec5d02391b7ff0383fc'    # 这行是你需要根据自己的情况修改的地方
# url = 'http://10.23.2.4/eportal/index.jsp?wlanuserip=50525b554b0c65a6304f42a91276d565&wlanacname=e8130dd9c88c8bf8f89b46fc0ae05c03&ssid=&nasip=e3da122140ddbef7db67d7cc0223f6b3&snmpagentip=&mac=1e44feae4f0a12f6b0e08c7651ae7e11&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=e8130dd9c88c8bf8f89b46fc0ae05c03&vid=9593a4d18664f1de&port=61e47cad1a7f4a94&nasportid=5b9da5b08a53a540cb3c232440f12fc3940e960c1d813d54ef234b42b50a3fc5'
url = 'http://10.8.2.2/eportal/success.jsp?userIndex=33363563666130393334333365333233653730383963326638633838643337395f3137322e32312e372e3132335f323032303231313232303731&keepaliveInterval=0'
#url = 'http://10.23.2.4/eportal/index.jsp?wlanuserip=1d90ec446c6b52bb80a013e0ee83ccd2&wlanacname=eb3dea19c415ccae600bdc9db5d15bde&ssid=512b4fa22cd47690c1d677b390465049&nasip=390c1cf6eea7dfbca3f3f0aca4b4d442&mac=20617c667d26c7015c5889cba8afcce5&t=wireless-v2&url=4be2aa94e61657a37b1da9b0c8748ec5d02391b7ff0383fc'
while(True):
    # response = requests.get(schoolWebURL)
    s = requests.session()
    response = request.urlopen(url)
    html = response.read()
    res = re.findall('<title>(.*)</title>', html.decode(encoding="GBK", errors="strict"))
    print('res:', res)
    title = ''
    if len(res) == 0:
        pass
    else:
        title = res[0]


    print("title:",title)
    if title == '登录成功':    # 根据上面的分析填入相应的字符
        print('登陆成功！')
    else:
        #先使用post
        postUrl = 'http://10.8.2.2/eportal/InterFace.do?method=login'
        data = {
            "userId": '202021122071',  # 这行是你需要根据自己的情况修改的地方
            "password": '0ae0cb1464bea4783513ad32b5b1226c59c56262cd3480c0ca513cb865476a0c0f046d76abd6a7f3eb448e6b644d5d4b80c9067745bf0de26b1a9c51e2a207b7022d6b62464741a1a5e1a749b5e4fd476af423e507e03ff0a61f7eb2417eb89aa654ce4e58a0dc5e48e2333c2c79b2e842487afc224bcfda4c04c0723ecce38f',  # 这行是你需要根据自己的情况修改的地方
            "queryString": 'wlanuserip%3D7c6ce76b7b9295fa44c39556fbe8a298%26wlanacname%3D355747ff48f3a490%26ssid%3D%26nasip%3D365cfa093433e323e7089c2f8c88d379%26snmpagentip%3D%26mac%3D369822c1132a6d3eee0c6bbcc068bed8%26t%3Dwireless-v2%26url%3D1a659010b267baf4dce8faba6abe221d805b7db3f1209582%26apmac%3D%26nasid%3D355747ff48f3a490%26vid%3D6969109da9c96d92%26port%3D7299524489fe792a%26nasportid%3Df68f49623ce287a7041122fb4f2c4f261598490372ea0880092f2394807216ba21605377e76f9280',
            "passwordEncrypt": 'true',
            "operatorPwd": '',
            "operatorUserId": '',
            "validcode": '',
            "service": '%E7%A7%BB%E5%8A%A8%E5%AE%BD%E5%B8%A6%E6%8E%A5%E5%85%A5',

        }
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Length": "955",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; EPORTAL_COOKIE_DOMAIN=false; EPORTAL_COOKIE_USERNAME=202021122071; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_NEWV=true; EPORTAL_COOKIE_PASSWORD=0ae0cb1464bea4783513ad32b5b1226c59c56262cd3480c0ca513cb865476a0c0f046d76abd6a7f3eb448e6b644d5d4b80c9067745bf0de26b1a9c51e2a207b7022d6b62464741a1a5e1a749b5e4fd476af423e507e03ff0a61f7eb2417eb89aa654ce4e58a0dc5e48e2333c2c79b2e842487afc224bcfda4c04c0723ecce38f; EPORTAL_COOKIE_SERVER=%E7%A7%BB%E5%8A%A8%E5%AE%BD%E5%B8%A6%E6%8E%A5%E5%85%A5; EPORTAL_COOKIE_SERVER_NAME=%E7%A7%BB%E5%8A%A8%E5%AE%BD%E5%B8%A6%E6%8E%A5%E5%85%A5; EPORTAL_USER_GROUP=%E5%AD%A6%E7%94%9F%E5%8C%85%E6%9C%88; JSESSIONID=3592ED7EF1F7DA3775286FFBC65C1E4D",
            "Host": "10.8.2.2",
            "Origin": "http://10.8.2.2",
            "Referer": "http://10.8.2.2/eportal/index.jsp?wlanuserip=7c6ce76b7b9295fa44c39556fbe8a298&wlanacname=355747ff48f3a490&ssid=&nasip=365cfa093433e323e7089c2f8c88d379&snmpagentip=&mac=369822c1132a6d3eee0c6bbcc068bed8&t=wireless-v2&url=1a659010b267baf4dce8faba6abe221d805b7db3f1209582&apmac=&nasid=355747ff48f3a490&vid=6969109da9c96d92&port=7299524489fe792a&nasportid=f68f49623ce287a7041122fb4f2c4f261598490372ea0880092f2394807216ba21605377e76f9280",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",

        }
        response = requests.post(postUrl, data, headers=header)
        print(response.encoding)
        print(response.text)
        uft_str = response.text.encode("iso-8859-1").decode('utf-8')
        print(uft_str)
        print("状态码{}".format(response))  # 打印状态码
        # 使用GET方式登录校园网
        schoolWebLoginURL = 'http://10.8.2.2/eportal/success.jsp?userIndex=33363563666130393334333365333233653730383963326638633838643337395f3137322e32312e372e3132335f323032303231313232303731&keepaliveInterval=0'
        response = requests.get(schoolWebLoginURL).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
        print("状态码{}".format(response))  # 打印状态码
    # 每10s检测一次是否成功连接
    time.sleep(10)
