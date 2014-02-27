#encoding:utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('form.html')
dr.get(file_path)

#选中checkbook
#dr.find_element_by_css_selector('input[type=checkbox]').click()
dr.find_element_by_class_name('checkbox').click()
sleep(1)

#选中radio
dr.find_element_by_css_selector('input[type=radio]').click()
sleep(1)

#选中下拉菜单中的最后一项
dr.find_element_by_tag_name('select').find_elements_by_tag_name('option')[-1].click()
sleep(1)

#点击提交按钮
dr.find_element_by_css_selector('input[type=submit]').click()
sleep(10)

alert = dr.switch_to_alert()	#定位到提示框
print alert.text			#打印出提示框的文本信息
alert.accept()			#接受提示，相当于点击确定
dr.quit()