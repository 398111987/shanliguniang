# coding:utf-8
from appium import webdriver
import time
desired_caps = {'platformName':'Android',
                'deviceName':'4.4.2',
                'platformVersion':'M9N7N15710006501',
                'appPackage':'com.nngdjt.app',
                'appActivity':'com.nngdjt.app.m00_welcome.LaunchActivity'}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
time.sleep(30)
#获取到当前页面所有的环境
contexts = driver.contexts
print contexts

#点击乘客服务
