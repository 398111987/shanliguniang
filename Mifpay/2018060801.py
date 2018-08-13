# coding:utf-8
#--coding:gb18030--
import unittest
import os,sys,StringIO
from unittest import TestSuite

from appium import webdriver
import HTMLTestRunner
from time import sleep
import time

#执行测试的类
class Dttest(unittest.TestCase):
     def setUp(self):
        #测试前需要执行的操作
        print("start setup")
        desried_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4.2',
            'deviceName': 'd093b839',
            'appPackage': 'com.nngdjt.app',
            'appActivity': 'com.nngdjt.app.m00_welcome.LaunchActivity'
            }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desried_caps)
        sleep(5)
     def tearDown(self):
        #测试用例执行完成后需要执行的操作
         self.driver.quit()
         print("tearDown")

     def test_logout(self):
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click() # 点击“我的”
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()   #点击用户名显示位置
         self.driver.find_element_by_id("com.nngdjt.app:id/tvSafeLogout").click()  #点击安全退出
         #点击确认退出
         self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
         sleep(5)

     def test_Login(self):       #登录
        #若已经是登录状态则先退出
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  #点击“我的”
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击用户名显示位置
         try:
             el = self.driver.find_element_by_id("com.nngdjt.app:id/tvSafeLogout").click() #判断是否有“安全退出”按钮
             if e1 is not None:
                 el.click()  # 点击安全退出
                 # 点击确认退出
                 self.driver.find_element_by_link_text(u"确认退出").click()
                 self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000016')  # 输入手机号
                 self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123*")  # 输入密码
                 self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()  # 点击“登录”
         except Exception as e:
                 self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  #点击“注册/登录”
                 self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000016')  #输入手机号
                 self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123*")  #输入密码
                 self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()  #点击“登录”

     def test_forgetpwd(self): #忘记密码
        self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  #点击我的
        self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  #点击注册登录
        self.driver.find_element_by_id("com.nngdjt.app:id/btnResetpwd").click()    #点击忘记密码

        self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").sendkeys("13700000016")  #输入手机号
        self.driver.find_element_by_id("com.nngdjt.app:id/btnSend").click()        #点击获取验证码
        self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealShow").sendkeys("abc123*")  #输入密码
        self.driver.find_element_by_id("com.nngdjt.app:id/btnConfirm").click()    #点击完成

if __name__ == '__main__':
    unittest.main()








