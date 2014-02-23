#encoding:utf-8
#前进和后退的方法

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
first_url = 'http://www.baidu.com'
print "now acces %s" % first_url

dr.get(first_url)
sleep(1)

sencod_url = 'http://news.baidu.com/'
print "now acces %s" % sencod_url

dr.get(sencod_url)
sleep(1)
print "back to %s" % first_url
dr.back()
sleep(1)
print "forward to %s" % sencod_url
dr.forward()
sleep(1)
dr.quit()


