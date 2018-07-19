from __future__ import print_function

import urllib,http
from bs4 import BeautifulSoup
import sys,os,csv

def addReqHeader(req):
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    req.add_header('Upgrade-Insecure-Requests', '1')
    req.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Cache-Control', 'max-age=0')
    req.add_header('Accept-Language', 'en-US,en;q=0.8,pt;q=0.6')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Cookie', 'sessionid=13cxrt4uytfc6ijvgeoflmb3u9jmjuhil; csrftoken=jdEKPN8iL62hdaq1hmMuID9DMALiiDIq')
    return req

def getMarket(market):
    mylist=[]
    try:
        url = "https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange="+market+"&render-download"
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
        req.add_header('Upgrade-Insecure-Requests', '1')
        req.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Cache-Control', 'max-age=0')
        req.add_header('Accept-Language', 'en-US,en;q=0.8,pt;q=0.6')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req = addReqHeader(req)
        print(req.headers)
        
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            wrapper = csv.reader(the_page.strip().split('\n'))
            count = 0
            for record in wrapper:
                if count == 0:
                    count += 1
                    pass
                else:
                    mylist.append(record)
    except (urllib.error.URLError, urllib.error.HTTPError, http.HTTPException) as e:
        count = 0
    return mylist

#structure[date,close,volume,open,high,low]
#period[1d,1m,3m,6m,1y,18m,2y,3y,4y,5y,6y,7y,8y,9y,10y]
def getHistory(period,symbol):
    mylist = []
    try:
        url = 'http://www.nasdaq.com/symbol/'+ symbol.lower() +'/historical'
        print('link={}'.format(url))
        req = urllib.request.Request(url)
        req = addReqHeader(req)
        print(req.headers)
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            soup = BeautifulSoup(the_page,'lxml')
            myinput = soup.find('input',{"id","__VIEWSTATE"})
            data1 = myinput['value']
            myinput = soup.find('input',{"id","__VIEWSTATEGENERATOR"})
            data2 = myinput['value']
            myinput = soup.find('input',{"id","__VIEWSTATEENCRYPTED"})
            data3 = myinput['value']
            myinput = soup.find('input',{"id","__EVENTVALIDATION"})
            data4 = myinput['value']
            myinput = soup.find('input',{"id","quotes_content_left_submitString"})
            data5 = period + '|true|' + symbol
            data = {'__VIEWSTATE':data1,'__VIEWSTATEGENERATOR':data2,'__VIEWSTATEENCRYPTED':data3,'__EVENTVALIDATION':data4,'ctl00$quotes_content_left$submitString':data5}
            data = bytes(urllib.urlencode(data).encode())
        try:
            hendler = urllib.urlopen(url,data)
            wrapper = csv.reader(handler.read(),decode('utf-8').strip().split('\n'))
            print(wrapper)
            count = 0
            for record in wrapper:
                if count < 2:
                    count += 1
                    pass
                else:
                    mylist.append(record)
        except (urllib.error.URLError,urllib.error.HTTPError,http.HTTPException) as e:
            count = 0
    except (urllib.error.URLError,urllib.error.HTTPError,httplib.HTTPException) as e:
        count = 0
    return mylist

def getSymbol(inputlist):
    mylist=[]
    for item in inputlist:
        mylist.append(item[0])
    return mylist


market = 'NASDAQ'
period = '1d'
thresold = 500

# market_list = getMarket(market)
# print(market_list)
# if not os.path.exists(market):
#     os.mkdir(market)

# with open(market+'/marketlist.csv','w') as output:
#     writer = csv.writer(output,lineterminator='\n')
#     writer.writerows(markeet_list)

# symbol = getSymbol(market_list)
history = getHistory(period,'AAPL')