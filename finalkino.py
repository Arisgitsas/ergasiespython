import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
dailymatches=[]
mynums=[15,2,21,1,4,5,9,18,57,74]
date1=[]
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    date1.insert(i,date_str)
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp))
    dailymatches.insert(i,0)
    for k in range(180):
        if r[i] > 4:
                dailymatches[i] = dailymatches[i] + 1
maxim = 0
for i in range(30):
    if dailymatches[i] > dailymatches[i+1]:
        maxim = dailymatches[i]
        maximp = i
print 5*"-"
print("most matches per day are "),maxim ,("and on the day of"),date1[maximp]
