#encoding:utf-8

from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('status.html')
dr.get(file_path)
text_field = dr.find_element_by_name('user')
print text_field.is_enabled()	#判断text_field元素是否置灰，是返回True

print dr.find_element_by_class_name('btn').is_enabled()
#隐藏text_field,判断其是否显示
dr.execute_script('$(arguments[0]).hide()', text_field)
print text_field.is_enabled()

radio = dr.find_element_by_name('radio')
radio.click()
print radio.is_selected()	#判断radio元素是否被选中，是返回true

#判断其元素是否存在
try:
	dr.find_element_by_id('none')
except:
	print 'element does not exist'

dr.quit()
