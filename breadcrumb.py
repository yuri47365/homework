#encoding:utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('breadcrumb.html')
dr.get(file_path)

#获得其父层级
for link in dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a'):
	print link.text

#获取当前层级
#由于页面上可能有多个class和active元素
#所以使用层级定位最保险

print dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text
dr.quit()