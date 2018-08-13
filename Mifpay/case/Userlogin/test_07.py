# coding:utf-8
from appium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Firefox()
driver.get("https://www.cnblogs.com/shanliguniang/")
try:
    element = driver.find_element("id","blog_nav_newpostxx")
except NoSuchElementException as msg:
    print u"查找元素异常%s"%msg
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    t = driver.get_screanshot_as_file('%s.jpg'%nowTime)
    print(u"截图结果：%s"%t)
else:
    element.click()