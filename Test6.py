#encoding=utf-8



import sys

class Counts:

    def RestIndex(self):
        alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pre = 4
        listCount = len(alist)
        avg = listCount/pre
        for i in range(1, pre+1):
            start = avg * i - avg + 1
            if i == 1:
                start = 0
            end = avg * i
            if i == pre:
                end = listCount - 1
            print start, end



if __name__=='__main__':
    c = Counts()
    c.RestIndex()
