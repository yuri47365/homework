#encoding:utf-8

from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('wait.html')
dr.get(file_path)

dr.find_element_by_id('btn').click()

wait = ui.WebDriverWait(dr, 10)
wait.until(lambda dr: dr.find_element_by_class_name('label').is_displayed())
sleep(2)
dr.quit()


