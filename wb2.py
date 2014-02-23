#encoding:utf-8
#浏览器最大化maximize_window()

from selenium import webdriver
import time

dr = webdriver.Chrome()
time.sleep(2)
print "maximize browser"

dr.maximize_window()

time.sleep(2)
print "close browser"
dr.quit()