from flask import Flask
from flask_sockets import Sockets
import json
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
Sockets = Sockets(app)

sok = {}

@Sockets.route('/test')
def socketResponse(ws):
    # send = {}
    # send['msg'] = "hello"
    # send['faname'] = "钟科杰"
    # send['shouname'] = "陈霖"
    # send['toid'] = "1111"
    # ws.send(json.dumps(send))
    while not ws.closed:
        re = ws.receive()
        if re is not None:
            print("收到的信息为：" + re)
            id = re.id
            if id in sok.keys():
                print("此id已存在")
            else:
                sok.setdefault('id',ws)
        else:
            print("no receive")

@app.route('/')
def hello():
    return 'Hello World! server start！'

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()