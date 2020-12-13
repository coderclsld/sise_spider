from flask import Flask, request
from SchoolPlatform.spider import spider
app  = Flask(__name__)

@app.route('/kebiao',methods=['GET'])
def kebiao():
    username = request.args.get("username")
    password = request.args.get("password")
    print(username,password)
    sp = spider(username,password)
    a = sp.to_login()
    sp.student_schedular()
    return str(a)



if __name__ == "__main__":
    app.run(host='172.16.168.175',port=8001)