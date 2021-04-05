from huey import crontab

from app import huey
import time
import os
import sqlite3
from datetime import timedelta,datetime

uri = '/Users/xubiao/Downloads/huey-master/examples/flask_ex/demo.db'

max = datetime(9999,12,31,23,59)

@huey.task()
def example_task(n,app):
    # Example task -- prints the following line to the stdout of the
    # consumer process and returns the argument that was passed in (n).
    print('-- RUNNING EXAMPLE TASK: CALLED WITH n=%s --%s' % (n,str(app)))
    return n


@huey.periodic_task(crontab(minute='*/5'))
def print_every5_minutes():
    # Example periodic task -- this runs every 5 minutes and prints the
    # following line to the stdout of the consumer process.
    print('-- PERIODIC TASK -- THIS RUNS EVERY 5 MINUTES --')

f1= True
@huey.task()
def t1():
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    sql = 'select state from info where task = "t1"'
    c.execute(sql)
    state = c.fetchone()[0]
    global f1
    while f1:
        if state ==0 or state == '0' : 
            print('t1 exit 0')
            f1 = False
        time.sleep(1)
        cmd = 'ping -c 1 www.baidu.com'
        output = os.popen(cmd)
        print(output.read())

f2= True
@huey.task()
def t2():
    conn = sqlite3.connect(uri)
    c = conn.cursor()
    sql = 'select state from info where task = "t2"'
    c.execute(sql)
    state = c.fetchone()[0]
    while f2:
        if state ==0 : 
            print('t2 exit 0')
            return
        time.sleep(1)
        cmd = 'ping -c 1 www.google.com'
        output = os.popen(cmd)
        print(output.read())
        
        

@huey.task()
def stop_task(id):

    res = huey.revoke_by_id(id,revoke_until=max,revoke_once=False)
    print(r'revoke:=============================={}'.format(res))
