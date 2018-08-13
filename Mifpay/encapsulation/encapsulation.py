# -*- coding: utf-8 -*-
 3 # @Time    : 2018-06-11 09:20
 4 # encapsulation/encapsulation.py
 5
 6 # 封装部分维护在此
 7
 8 from config.config_01 import locat_config
 9 from log.log import Logger
111
12 from selenium.webdriver.support import expected_conditions as EC
13
14 class UIHandle():
15     logger = Logger()
16
17     # 构造方法，用来接收selenium的driver对象
18     @classmethod
19     def __init__(cls, driver):
20         cls.driver = driver
21
22     # 输入地址
23     @classmethod
24     def get(cls, url):
25         cls.logger.loginfo(url)
26         cls.driver.get(url)
27
28     # 关闭浏览器驱动
29     @classmethod
30     def quit(cls):
31         cls.driver.quit()
32
33     # element对象（还可加入try，截图等。。。）
34     @classmethod
35     def element(cls, page, element):
36         # 加入日志
37         cls.logger.loginfo(page)
38         # 加入隐性等待
39         # 此处便可以传入config_o1中的dict定位参数
40         el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(locat_config[page][element]))
41         # 加入日志
42         cls.logger.loginfo(page+'OK')
43         return el
44     # element对象(还未完成。。。)
45     def elements(cls, page, element):
46         # 加入日志
47         cls.logger.loginfo(page)
48         # 加入隐性等待
49         WebDriverWait(cls.driver, 10)
50         els = cls.driver.find_elements(*locat_config[page][element])
51         # 注意返回的是list
52         return els
53
54     # send_keys方法
55     @classmethod
56     def Input(cls, page, element, msg):
57         el = cls.element(page, element)
58         el.send_keys(msg)
59
60     # click方法
61     @classmethod
62     def Click(cls, page, element):
63         el = cls.element(page, element)
64         el.click()