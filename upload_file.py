#encoding:utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upload_file.html')
dr.get(file_path)

dr.find_element_by_name('file').send_keys('F:\webdriverex\upload_file.html')
sleep(2)
dr.quit()