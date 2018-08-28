# -*- coding: utf8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def distinct(filename):

    former = []
    f = open(filename, 'rb')
    for line in f:
        former.append(line.strip())
    length = len(former)
    print 'total number former: ' + str(length)
    print 'distincing...'
    list.sort(former)
    later = []
    define = former[0]
    later.append(define)
    for i in range(1, length):
        if define == former[i]:
            continue
        else:
            define = former[i]
            later.append(former[i])
    f.close()

    f = open(filename, 'wb')
    after_length = len(later)
    print 'total number later: ' + str(after_length)
    for i in range(0, after_length):
        f.write(str(later[i]) + "\n")
    f.close()

    return 0

if __name__ == '__main__':
    distinct('../weibo/weiboIdList.txt')

