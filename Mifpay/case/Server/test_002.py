# coding:utf-8
#--coding:gb18030--
from appium import webdriver
from selenium import webdriver
import time,os,unittest

def StartApp():
    try:
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
        time.sleep(5)
    except Exception as e:
        print(e)
        driver.get_screenshot_as_file("failed.jpg")
        return False
    return True
if __name__ =='__main__':
    if(True==StartApp()):
       print("StartApp OK")
    else:
        print("StartApp NOK")