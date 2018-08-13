# coding:utf-8
from appium import webdriver
import time
import os
desried_caps={
                     'platformName':'Android',
                     'platformVersion':'5.1.1',
                     'deviceName':'M9N7N15710006501',
                     'appPackage':'com.nngdjt.app',
                     'appActivity':'com.nngdjt.app.m00_welcome.LaunchActivity',
                     'noReset':True,
                     "unicodeKeyboard": True,
                     "resetKeyboard": True
                     }
driver = webdriver.Remote("http://localhost:4723/wd/hub",desried_caps)
time.sleep(30)
#获取到当前页面所有的环境
contexts = driver.contexts
print contexts

#点击乘客服务

fa_sun = '//*[@resoure-id="com.nngdjt.app:id/llContentDb"]/android.widget.TextView'