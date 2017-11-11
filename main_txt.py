
# -*- coding: utf-8 -*-

import urllib2
import os
import codecs
import csv
import cStringIO
from bs4 import BeautifulSoup

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

fileName = os.getcwd() + os.sep + "output.txt"
f = codecs.open(fileName, "w", 'utf-8')
#writer = UnicodeWriter(open(fileName, 'wb'), delimiter=',')


response = urllib2.urlopen("http://www.51ape.com/zhuanji/index_2.html")
#print response.read()

soup = BeautifulSoup(response, "html.parser")

ulCont = soup.find("ul", class_="mt_05 w638")
#print type(ulCont)
for linkCont in ulCont.find_all("a"):
    print linkCont['title'],linkCont["href"]
    #lines.append(linkCont['title'] + ',' + linkCont["href"] + '\n')
    line = linkCont['title'] + ',' + linkCont["href"] + '\r\n'
    #line = [linkCont['title'] , linkCont["href"]]
    f.write(line)
    #writer.writerow(line)

#print len(lines)
#f.writelines(lines)
f.close()





#for linkCont in soup.find_all("li", class_="blk_nav lh30 over"):
#    print linkCont