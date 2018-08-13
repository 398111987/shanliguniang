# coding:utf-8
import unittest
import os
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 用例路径
# case_path = os.path.join(os.getcwd(),"case")  #这种写法是被写死的，不好用
case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"case") #获取当前目录下的case目录

# 报告存放路径
report_path = os.path.join(os.getcwd(),"report")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover
if __name__ =="__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    report_path = "D:\\MissTest001\\report\\result.html"

    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description='用例执行情况：')

    runner.run(all_case())
    fp.close()


