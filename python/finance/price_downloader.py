from __future__ import print_function

import urllib2, csv, cookielib


link = "http://example.com"
r = urllib2.Request(url=link)
# r.add_header('Cookie', 'sessionid=13cxrt4uytfc6ijvgeoflmb3u9jmjuhil; csrftoken=jdEKPN8iL62hdaq1hmMuID9DMALiiDIq')
r.add_header('Upgrade-Insecure-Requests', '1')
r.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
r.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
r.add_header('Connection', 'keep-alive')
r.add_header('Cache-Control', 'max-age=0')
r.add_header('Accept-Language', 'en-US,en;q=0.8,pt;q=0.6')
r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
response = urllib2.urlopen(r)
print(response.read())

symbolTest = 'AAPL'
companylist = 'companylist_NASDAQ'

try:
    with open(companylist+'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Symbol'],row['Name'])
            symbol = row['Symbol'].strip()
            print(symbol)
            if '^' not in symbol:
                site = "http://xueqiu.com/"
            else:
                print('symbol contains ^')
except:
    pass