import requests as r
import re
import os
import sys
import webGet
import dict

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print("attribs too little, we need two attribs.")
        print('Type two attribs and then type enter key.')
        exit
    print('[searching on website]')
    a = argv[0]
    b = argv[1]
    webAdd = 'https://en.wikipedia.org/wiki/'
    webPost = ''
    # webAdd='https://cn.bing.com/search?q='
    # webPost='&qs=n&form=QBLH&sp=-1&pq=furude&sc=0-6&sk=&cvid=A07B1D0226E14E5D8585A15510974222'
    obj = dict.dict()
    lis = obj.data()

    wa = r.get(webAdd+a+webPost).text
    wb = r.get(webAdd+b+webPost).text
    print('[pairing infomation]')
    # fil = re.compile('<[^>]*>')
    # wa = fil.sub('', wa)
    # wb = fil.sub('', wb)
    # wa=webGet().filter_tags(wa)
    # wb=webGet().filter_tags(wb)
    wa=webGet.webGet().filter_tags(wa)
    wb=webGet.webGet().filter_tags(wb)
    na = []
    nb = []
    for i in lis:
        if i in wa:
            na.append(1)
        else:
            na.append(0)
        if i in wb:
            nb.append(1)
        else:
            nb.append(0)
    sum = 0
    for i in range(len(na)):
        if na[i] == nb[i]:
            sum = sum+1
            # print(lis[i])
    print('[similarity]'+str(sum/len(na)))
