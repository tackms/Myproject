#encoding=utf-8




class TrimTest:


    def trim(self,s):
            if s[:1] == ' ':
                s = s[1:]
            if s[:-1] == ' ':
                s = s[-1:]
            return s


    def trim1(self,s):
         return s.strip()


if __name__ == '__main__':
    s = ' aa b '
    trim = TrimTest()
    a = trim.trim(s)
    b = trim.trim1(s)
    print (a)
    print(b)