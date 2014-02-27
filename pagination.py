#encoding:utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('pagination.html')
dr.get(file_path)

#获取所有分页的数量，-2(去掉上一个和下一个)
total_pages = len(dr.find_element_by_class_name('pagination').find_elements_by_tag_name('li')) - 2
print 'total pages is %s' % total_pages

#获取当前页面是第几页
current_page = dr.find_element_by_class_name('pagination').find_element_by_class_name('active')
print 'current page is %s' % current_page.text
dr.quit()