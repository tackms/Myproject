# encoding=utf-8

import urllib2
import re

class BDTB:

    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print '连接错误！',e.reason
                return None


    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1).strip()
            return result.group(1).strip()
        else:
            return None


    def getPageNum(self):
        page =self.getPage(1)
        pattern = re.compile('li class="l_reply_num.*?</span>.*?<span.*?(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None


if __name__ == '__main__':
    baseUrl = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseUrl, 1)
    #bdtb.getPage(1)
    bdtb.getPageNum()