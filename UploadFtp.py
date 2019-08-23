#encoding=utf-8



import sys
import os
import time
from ftplib import FTP


cur_date = time.strftime('%Y-%m-%d %H:%m:%s',time.localtime(time.time()))
bizdate = time.strftime('%Y-%m-%d %H:%m:%s',time.localtime(time.time()))[0,8]

class Xfer(object):

    def __init__(self):
        self.ftp = None

    def __del__(self):
        pass

    def setFtpParams(self, ip, uname, pwd, port = 8021, timeout = 60):
        self.ip = ip
        self.uname = uname
        self.pwd = pwd
        self.port = port
        self.timeout = timeout

    def initEnv(self):
        if self.ftp is None:
            self.ftp = FTP()
            print  ('###%s Connect ftp server : %s ....'%(cur_date,self.ip))
            self.ftp.connect(self.ip , self.port , self.timeout)
            self.ftp.login(self.uname , self.pwd)
            print (self.ftp.getwelcome())

    def clearEnv(self):
        if self.ftp:
            self.ftp.close()
            print ('###% Disconnect ftp server: %s!'%(cur_date,self.ip))
            self.ftp = None

    def rename(self,path):
        files = os.listdir(path)
        fname = path.split('/')[-1]
        for file in files:
            olddir = os.path.join(path,file)
            ftmp = olddir.split('.')[-1]
            if os.path.isdir(olddir):
                continue;
            filetype = os.path.splitext(file)[0] + os.path.splitext(file)[1] + ".unimastmp"
            newdir = os.path.join(path,filetype)
            if ftmp == 'unimastmp':
                pass
            else:
                os.rename(olddir,newdir)

    def file_del(self,localdir):
        files = os.listdir(localdir)
        fname = localdir.split('/')[-1]
        suc = localdir + '/' + fname + '_SUCCESS' + '.unimastmp'
        item = os.listdir(localdir)
        for i in item:
            p = os.path.join(localdir, i)
            if len(item) == 1 and p == suc:
                print ("del file %s")%p
                os.remove(p)
            else:
                break

    def file_count(self,path):
        try:
            p = os.popen("du -sh %s"%path)
            print p.read()
            havefile = len(os.listdir(path))
            if havefile >= 1:
                p1 = os.popen("cat %s/*|wc -l"%path)
                print 'total number of articles:',p1.read()
        except Exception as e:
            s = sys.exc_info()
            print "[Error %s hanppened on line %d"%(s[1],s[2].tb_lineno)

    def uploadFile(self,localdir,remotepath='./'):
        try:
            if not os.path.isdir(localdir):
                return
            n = 1
            for file in os.listdir(localdir):
                localpath = os.path.join(localdir, file)
                path = localpath.split('/')[-2]
                if len(localpath.split('/')) == 5:
                    tablename = localpath.split('/')[3]
                dir  = self.ftp.nlst()

                if dir.count(path) == 0:
                    print "dir %s not exist,create is"%(path)
                    self.ftp.mkd(path)
                print '+++Upload %s to %s:%s'%(localpath,self.ip,file)
                self.ftp.cwd(path)
                if self.ftp.storbinary('STOR' + file,open(localpath,'rb')):
                    print 'OK File upload success'
                    self.ftp.rename(file,file[0:-9]+'txt')
                    os.remove(localpath)
                    dodo.succeed()
                else:
                    dodo.fail()
                self.ftp.cwd('..')
        except Exception as e:
            s = sys.exc_info()
            print "[Error %s hanppened on line %d"%(s[1],s[2].tb_lineno)


    def getinfo(self,path):
        record_size_path = '/home/upload/log/upload_size_record.txt'
        havefile = len(os.listdir(path))
        try:
            if havefile >=1:
                if os.path.getsize(path) == 6:
                    print ("file is empty!")
                else:
                    path_split = path.split('/')
                    len_path = len(path_split)
                    tablename = path_split[int(len_path)-1]
                    total1 = os.popen("cat %s/*|wc -1"%(path))
                    total = total1.read()
                    size1 = os.popen("du -sh %s"%(path))
                    size = size1.read()
                    size = size.replace(' ','')
                    size = size.split('/')[0]
                    info_str = "%s|%s|%s|%s|%s| success"%(tablename.strip(),cur_date.strip()
                                                          ,total.strip(),size.strip(),bizdate.strip())
                    print info_str
                    with open(record_size_path,'a+') as info:
                        info.write(info_str +'\n')
                    info.close()
        except Exception as e:
            s = sys.exc_info()
            print s

    def upload(self,localdir):
        self.initEnv()
        self.uploadFile(localdir,remotepath='./')
        self.clearEnv()
        time.sleep(1)



if __name__ == '__main':

  srcDir = sys.argv[1]
  xfer = Xfer()
  xfer.setFtpParams('10.14.152.218','send','qazwsx')
  xfer.file_count(srcDir)
  xfer.rename(srcDir)
  xfer.getinfo(srcDir)
  xfer.upload(srcDir)
  xfer.file_del(srcDir)









