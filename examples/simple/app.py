from flask import Flask,request
import json

app = Flask(__name__)


@app.route('/test',methods=['POST'])
def test():

    from tasks import add
    i = request.json['i']
    j = request.json['j']
    res = add(i,j)
    print('Result:',type(res),res.id)
    # ret = res.get(True)
    # print(ret)
    return json.dumps({'id':res.id})

@app.route('/cancle',methods=['POST'])
def cancle():
    from tasks import cancle_task
    id = request.json['id']
    cancle_task(id)
    return 'done'


    return 'done'
if __name__ == '__main__':
    app.run('0.0.0.0',5678)