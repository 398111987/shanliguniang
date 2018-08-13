# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print "end!"

    def test_login(self):
    # 若已经是登录状态则先退出
    self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  # 点击“我的”
    self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击用户名显示位置
    try:
        el = self.driver.find_element_by_id("com.nngdjt.app:id/tvSafeLogout").click()  # 判断是否有“安全退出”按钮
        if e1 is not None:
            el.click()  # 点击安全退出
            # 点击确认退出
        self.driver.find_element_by_link_text(u"确认退出").click()
        self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000034')  # 输入手机号
        self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123")  # 输入密码
        self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()  # 点击“登录”
    except Exception as e:
        #    self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  #点击“注册/登录”
        self.driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000034')  # 输入手机号
        self.driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123")  # 输入密码
        self.driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()  # 点击“登录”

    def test_logout(self):
        self.driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  # 点击“我的”
        self.driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击用户名显示位置
        self.driver.find_element_by_id("com.nngdjt.app:id/tvSafeLogout").click()  # 点击安全退出
        # 点击确认退出
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
        sleep(5)


