# coding:utf-8
from time import sleep
def test_passgerserver():
    # 点击“点我乘车”
    driver.find_element_by_id("com.nngdjt.app:id/tvMainTitle").click()
    sleep(10)

    # 这里要先判断是否已经登录了，若没有登录则先登录
    try:
        e1 = driver.find_element_by_id("com.nngdjt.app:id/tvToolbarTitle")
        driver.find_element_by_id("com.nngdjt.app:id/edtMobileReal").send_keys('13700000024')
        driver.find_element_by_id("com.nngdjt.app:id/edtPasswordRealHide").send_keys("abc123")
        driver.find_element_by_id("com.nngdjt.app:id/btnLoginConfim").click()
        sleep(30)
        # 未检测到闸机，关闭弹出提示框
        e3 = driver.find_element_by_id("android:id/button1")
        if e3 is not None:
            e3.click()
        driver.find_element_by_class_name("android.widget.ToggleButton").click()
        ac = driver.current_activity
        print(ac)
        driver.wait_activity("ac", 30)
        print("haha")

        driver.find_element_by_id("android:id/button1").click()
        # 从刷机页面返回首页
        driver.find_element_by_class_name("android.widget.ImageButton").click()

    except Exception as e:
        ac2 = driver.current_activity
        print(ac2)
        driver.wait_activity(ac2, 30)
        driver.find_element_by_id("android:id/button1").click()  # 点击按钮“知道了”
        driver.find_element_by_class_name("android.widget.ToggleButton").click()
        sleep(20)
        driver.find_element_by_class_name("android.widget.ImageButton").click()
        # 从刷机页面返回首页
        driver.find_element_by_class_name("android.widget.ImageButton").click()