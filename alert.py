#encoding:utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('alert.html')
dr.get(file_path)

#点击链接
dr.find_element_by_id('tooltip').click()
sleep(2)

try:
	alert = dr.switch_to_alert()
	alert.accept()
	#dr.switch_to_alert().accept()
except:
	print 'no alerts display'

sleep(1)
dr.quit()