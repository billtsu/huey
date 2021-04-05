from flask import render_template
from flask import request,current_app

from app import app
from tasks import example_task,t1,t2,stop_task
import json

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('n'):
        n = request.form['n']

        # Enqueue our task, the consumer will pick it up and run it.
        with app.app_context():
            example_task(n,current_app)
        message = 'Enqueued example_task(%s) - see consumer output' % n
    else:
        message = None

    return render_template('home.html', message=message)

@app.route('/b')
def b():
    id = t1().id
    return 't1 started {}'.format(id)

@app.route('/g')
def g():
    id = t2().id
    return 't2 started {}'.format(id)

@app.route('/stop',methods = ['POST'])
def stop():
    import sys
    print(request.data)
    sys.stderr.write('{}'.format(request.data))
    data = request.json
    # data = json.load(request.data)
    
    id = data['id']
    stop_task(id)
    return ''


