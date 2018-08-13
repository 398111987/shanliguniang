# coding:utf-8
def test_forgetpwd(phoneid,password):  # 忘记密码

    driver.find_element_by_id("com.nngdjt.app:id/rdoPersonal").click()  # 点击我的
    driver.find_element_by_id("com.nngdjt.app:id/tvLogin").click()  # 点击注册登录
    driver.find_element_by_id("com.nngdjt.app:id/btnResetpwd").click()  # 点击忘记密码

    driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").sendkeys("phoneid")  # 输入手机号
    driver.find_element_by_id("com.nngdjt.app:id/btnSend").click()  # 点击获取验证码
    driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealShow").sendkeys("password")  # 输入密码
    driver.find_element_by_id("com.nngdjt.app:id/btnConfirm").click()  # 点击完成