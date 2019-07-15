# @Version : 1.0  
# @Time    : 2019/5/5  
# @Author  : 实小楼

import json
import urllib.request

api_url = "http://openapi.tuling123.com/openapi/api/v2"
print('实小楼：你好，我是你的实验助理小楼，今天聊点什么呢？')

a = 0

while 1:
    text_input = input('我：')
    
    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },
        },

        "userInfo": 
        {
            "apiKey": "7c10c126ce444271ab2d45c3e42f5bcd",
            "userId": "shiyanlou"
        }
    }

    req = json.dumps(req).encode('utf8')

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')

    response_dic = json.loads(response_str)


    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    
    print('实小楼：'+ results_text)
    
    a +=1
    
    if a>3:
        print('好了，今天聊得够多了，等你学会了我的代码，说不定我能多陪你聊几个小时，继续学习哦～')
        break
    