#encoding:utf-8
from selenium import webdriver

ff = webdriver.Firefox()
ff.implicitly_wait(10)

ff.get("http://somedomain/url_that_delays_loading")
myDynamicElement = ff.find_element_by_id('myDynamicElement')
'''
try:
	myDynamicElement = ff.find_element_by_id("myDynamicElement")
except:
	print 'element does not exist'
'''
ff.quit()