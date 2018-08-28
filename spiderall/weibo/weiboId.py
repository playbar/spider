# -*-coding:utf8-*-
from weibo import weiboIdList
# from Tool.distinct import distinct
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':

    f = open('weiboIdList.txt', 'r')
    length_old = 100000
    length_new = len(f.readlines())
    print 'list range : ' + 'from ' + str(length_old) + ' to ' + str(length_new)
    f.close()

    while (length_new != length_old):
        f = open('weiboIdList.txt', 'r')
        ids = []
        for line in f:
            ids.append(line.strip())
        f.close()

        for id in ids[length_old:length_new]:
            # print id
            print ids.index(id)
            weiboIdList(id)

        # distinct('weiboIdList.txt')
        f = open('weiboIdList.txt', 'r')
        length_old = length_new
        length_new = len(f.readlines())
        print 'list range : ' + 'from ' + str(length_old) + ' to ' + str(length_new)
        f.close()
