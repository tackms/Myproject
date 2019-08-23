#encoding=utf-8



class ResultIndex(object):


    def CountIndex(self):
            alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            item = 7
            startIndex = 0
            endIndex = len(alist) - 1
            while endIndex >= startIndex:
                mid = (startIndex + endIndex)/2
                guess = alist[mid]
                if guess == item:
                    return mid
                if guess > item:
                    endIndex = mid - 1
                else:
                    startIndex = mid + 1


if __name__ == '__main__':
    a = ResultIndex()
    b = a.CountIndex()
    print b

