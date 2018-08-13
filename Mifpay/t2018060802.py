# coding:utf-8
#--coding:gb18030--
import unittest
import os,sys,StringIO
from unittest import TestSuite
from selenium import webdriver
import time, os, unittest
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
            'platformVersion': '5.1.1',
            'deviceName': 'M9N7N15710006501',
            'appPackage': 'com.nngdjt.app',
            'appActivity': 'com.nngdjt.app.m00_welcome.LaunchActivity'

            }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desried_caps)
        sleep(5)
        print(self.driver.get_window_size())
        sleep(5)
        self.swipLeft(self.driver, t=800, n=3)
        self.driver.find_element_by_id("com.nngdjt.app:id/btnExperience").click()  # 点击立即体检
        self.driver.find_element_by_id("com.nngdjt.app:id/btn_next").click()  # 点击下一步
        self.driver.find_element_by_id("com.nngdjt.app:id/btn_close").click()  # 点击关闭

     def swipLeft(self,driver, t=500, n=1):
         '''向左滑动屏幕'''
         l = self.driver.get_window_size()
         x1 = l['width'] * 0.75
         y1 = l['height'] * 0.5
         x2 = l['width'] * 0.25
         for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

     # 测试用例执行完成后需要执行的操作
     def tearDown(self):
         #要考虑session退出的时间
         sleep(60)
         self.driver.quit()
         print("tearDown")

     def logout(self):
         #若已经登录的就退出登录
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click() # 点击“我的”
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()   #点击用户名显示位置
         self.driver.find_element_by_id("com.nngdjt.app:id/tvSafeLogout").click()  #点击安全退出
         #点击确认退出
         sleep(5)
         self.driver.tap([(48, 1428), (1032, 1572)], 100)

     def login(self,phoneid,password):
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()
         self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('phoneid')
         self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("password")
         self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()

     def test_login(self):
         # 若已经是登录状态则先退出
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  # 点击“我的”
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击用户名显示位置
         self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").clear()
         self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000034')  # 输入手机号
         self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").clear()
         self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123")  # 输入密码
         ac1 = self.driver.current_activity
         print(ac1)
         self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()  # 点击“登录”
         sleep(5)
         # 获取当前页面的Activity
         ac2 = self.driver.current_activity
         print(ac2)
         if ac2 != ac1:
             print(u"登录成功,跳转到下一个界面")
             self.logout()
             sleep(5)
             print(u"退出登录")

     def test_forgetpwd(self): #忘记密码
        self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  #点击我的
        self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  #点击注册登录
        self.driver.find_element_by_id("com.nngdjt.app:id/btnResetpwd").click()    #点击忘记密码

        self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys("13700000034")  #输入手机号
        self.driver.find_element_by_id("com.nngdjt.app:id/btnSend").click()        #点击获取验证码
        self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealShow").send_keys("abc123")  #输入密码
        self.driver.find_element_by_id("com.nngdjt.app:id/btnConfirm").click()    #点击完成
        sleep(10)

     def test_PassengerRide(self):  # 点击乘车
         self.login('13700000034','abc123')
         # 点击“点我乘车”
         self.driver.find_element_by_id("com.nngdjt.app:id/tvMainTitle").click()
         #区分是否能接收到闸机信号的情况
         self.driver.find_element_by_id("com.nngdjt.app:id/btn_close").click()
         #self.driver.find_element_by_class_name("android.widget.ToggleButton").click()  #点击刷机按钮
         sleep(30)
         # 从刷机页面返回首页
         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
         # 退出登录
         self.logout()

     def test_register(self):  # 未注册的手机号登录
         self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  #点击我的
         self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()    #点击注册/登录
         self.driver.find_element_by_id("com.nngdjt.app:id/btnModeSwitch").click()    #点击“注册”
         self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('15600006106') #输入手机号
         self.driver.find_element_by_id("com.nngdjt.app:id/btnSend").click()   #点击获取验证码
         sleep(3)
         self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealShow").send_keys('abc123') #输入密码
         self.driver.find_element_by_id("com.nngdjt.app:id/btnRegisterConfim").click()  #点击注册
         sleep(5)
         self.driver.find_element_by_id("com.nngdjt.app:id/btn_close").click()   #点击弹出的“知道了”


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest((Dttest('test_login')))
    suite.addTest((Dttest('test_register')))
    suite.addTest((Dttest('test_PassengerRide')))
    suite.addTest((Dttest('test_forgetpwd')))
    timestr = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'D:\\test2\\report\\' + timestr + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='result', description='report',verbosity=2)
    # 执行测试
    runner.run(suite)
    fp.close()








