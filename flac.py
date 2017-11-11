
# -*- coding: utf-8 -*-

import urllib2
import os
import time
from support import UnicodeWriter
from bs4 import BeautifulSoup

def crawl_flac():
    fileName = os.getcwd() + os.sep + "output_flac.csv"
    writer = UnicodeWriter(open(fileName, 'wb'), delimiter=',')
    writer.writerow([u"歌曲名", u"无损类型", u"内部路径", u"文件大小", u"百度云路径", u"提取码"])

    urls = []
    for i in range(1, 101):
        if i == 1:
            urls.append('index.html')
        else:
            urls.append('index_%d.html' % i)

    # print urls

    for url in urls:
        response = urllib2.urlopen("http://www.51ape.com/flacyinyue/%s" % url)
        #print response.read()

        soup = BeautifulSoup(response, "html.parser")

        ulCont = soup.find("ul", class_="mt_05")
        #print type(ulCont)
        for linkCont in ulCont.find_all("a"):
            print linkCont.get_text(), linkCont["href"]
            row = linkCont.get_text().rsplit('.', 1)
            row.append(linkCont["href"])
            row.append(linkCont.next_sibling.next_sibling.text)

            #print row[2]
            response = urllib2.urlopen(row[2])
            soup = BeautifulSoup(response, "html.parser")
            panCont = soup.find("a", class_="blue a_none")
            row.append(panCont["href"])

            codeCont = soup.find("b", class_="mt_1 yh d_b")
            row.append(codeCont.text.split(u"：")[1]);

            writer.writerow(row)

        time.sleep(10)

    return