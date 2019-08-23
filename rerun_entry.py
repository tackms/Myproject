#encoding = utf-8


import pymysql
import time
import os

for rerun_task import CheckRerunTask
bizdate = time.strftime('%Y%m%d',time.localtime(time.time()))

class RerunEntey():
    def __init__(self):
        self.db = None
        self.conn_mysql()

    def conn_mysql(self):
        self.db = pymysql.connect(host='172.19.60.72' , port =3306, user='root'
                                  ,passwd ='')
        if self.db:
            print "数据库连接成功！"
            self.cursor = self.db.cursor()

    def get_fail_check(self):
        _sql = "select..."
        self.cursor.execute(_sql)
        res = self.cursor.fetchall()
        instanceId_list = []
        os.system(':> /data/tsk/gyy_rerun_records.txt')
        with open('/data/task/gyy_rerun_records.txt','a') as records:
            for line in res:
                filename = line[0]
                instanceId = line[2]
                instanceId_list.append(instanceId)
                str = '%s\n'%(filename)
                records.write(str)
        return instanceId_list

    def __del__(self):
        if self.db:
            self.db.cloas()
            self.cursor.close()
            self.db = None
            print "数据库已断开！"


if __name__ == '__main__':
    obj = RerunEntey()
    ins_res = obj.get_fail_check()
    reobj = CheckRerunTask()
    for row  in ins_res:
        reobj.rerun(row)
        time.sleep(1)
