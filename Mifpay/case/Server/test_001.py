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
#driver.find_element_by_id("com.nngdjt.app:id/tvContentName").click()
#driver.find_element_by_class("android.widget.TextView").click()
#driver.find_element_by_xpath("//*[@text='站点信息'] ").click()

#driver.find_element_by_accessibility_id("站点信息").click()  #行不通
#driver.find_element_by_class_name("android.widget.TextView").click()

#用坐标定位 乘客服务  --OK 但要考虑到适配其他手机屏幕的问题，不建议使用坐标定位
adb = 'adb shell input tap 100 1350'  #点击乘客服务
os.system(adb)

driver.back()
time.sleep(2)

# 点击时刻表
driver.find_element_by_link_text("时刻表").click()    #不支持这种定位方式

#只能考虑Xpath定位







# #切换到webview
# #driver.switch_to.content(contexts[1])
# driver.switch_to.default_content(contexts[1])
# #获取当前的环境，看是否切换成功
# now = driver.current_context
# print now
# driver.find_element_by_id("com.android.browser:id/tvContentName").click()
#
# #切回native
# driver.switch_to.default_content(contexts[0])
# #获取当前的环境，看是否切换成功
# now = driver.current_context
# print now

