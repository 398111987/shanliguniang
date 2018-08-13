# coding:utf-8
#--coding:gb18030--
from appium import webdriver
from selenium import webdriver
import time,os,unittest


def test_register(self):  # 未注册的手机号登录
    self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  # 点击我的
    self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击注册/登录
    self.driver.find_element_by_id("com.nngdjt.app:id/btnModeSwitch").click()  # 点击“注册”
    self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('15600006106')  # 输入手机号
    self.driver.find_element_by_id("com.nngdjt.app:id/btnSend").click()  # 点击获取验证码
    sleep(3)
    self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealShow").send_keys('abc123')  # 输入密码
    self.driver.find_element_by_id("com.nngdjt.app:id/btnRegisterConfim").click()  # 点击注册
    sleep(5)
    self.driver.find_element_by_id("com.nngdjt.app:id/btn_close").click()  # 点击弹出的“知道了”

