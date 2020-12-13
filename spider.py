import json
import requests
import re

class spider(object):
    url = 'http://class.sise.com.cn:7001/sise/'
    toLogin_url = 'http://class.sise.com.cn:7001/sise/login_check_login.jsp'
    JSESSIONID = ''
    random = ""
    post_key = 333
    post_value = ''
    username=''
    password=''
    list_4 =""
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def get_values(self):
        request = requests.get(self.url)
        html = request.content.decode('GBK')
        print(html)
        self.JSESSIONID = request.cookies.get('JSESSIONID')
        print("self.JSESSIONID:"+self.JSESSIONID)
        self.random = re.findall('<input id="random"   type="hidden"  value="(.*?)"  name="random" />',html,re.S)[0]
        values = re.findall('<input type="hidden"(.*?)>',html,re.S)[0]
        print("values:"+values)
        self.post_key = re.findall('name="(.*?)"',values,re.S)[0]
        print("self.post_key:"+self.post_key)
        self.post_value = re.findall('value="(.*?)"',values,re.S)[0]
        print("self.post_value:"+self.post_value)

    def to_login(self):
        self.get_values()
        headers = {
            'Host': 'class.sise.com.cn:7001',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '172',
            'Origin': 'http://class.sise.com.cn:7001',
            'Connection': 'close',
            'Referer': 'http://class.sise.com.cn:7001/sise/',
            'Cookie': 'JSESSIONID='+self.JSESSIONID,
            'Upgrade-Insecure-Requests': '1',
        }
        data = {
            self.post_key:self.post_value,
            'random':self.random,
            'username':self.username,
            'password':self.password,
        }
        print("post_key:"+data[self.post_key])
        print("random:" + data['random'])
        print("username:" + data['username'])
        print("password:" + data['password'])
        result = requests.post(self.toLogin_url,headers=headers,data=data).content.decode('GBK')
        print("result:"+result)
        self.student_schedular()
        return self.list_4

    def list_split(self,items,n):
        return[items[i:i+n] for i in range (0,len(items) ,n)]


    def student_schedular(self):
        headers = {
            'Host': 'class.sise.com.cn:7001',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            'Referer': 'http://class.sise.com.cn:7001/sise/module/student_states/student_select_class/main.jsp',
            'Cookie': 'JSESSIONID='+self.JSESSIONID,
            'Upgrade-Insecure-Requests': '1',
        }
        url = 'http://class.sise.com.cn:7001/sise/module/student_schedular/student_schedular.jsp'
        student_class_html = requests.post(url,headers=headers)
        student_class_html.encoding = "GBK"
        print(student_class_html)
        print("clsld")
        student_class_html = student_class_html.text.replace('<br>','')
        MySchedular_dict = re.findall("class='font12'>(.*?)</td>",student_class_html,re.S)
        print(MySchedular_dict)
        list_2 = self.list_split(MySchedular_dict, 8)
        list_3 = eval(str(list_2))
        print(list_3[0][0])
        self.list_4 = json.dumps(list_2,ensure_ascii=False)
        print(self.list_4)


# if __name__ == '__main__':
#     to_login(1840915119,110120)
    # username = "1840915119"
    # password = "110120"
    # # MyScse_login = MyScse_login(username, password)
    # # if not MyScse_login.to_login():
    # if not to_login():
    #     print('获取失败！！！')
    # # MyScse_login.student_schedular()
    # student_schedular()
