# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print "end!"
    def test04(self):
        print "执行测试用例04"
    def test05(self):
        print "执行测试用例05"
    def test06(self):
        print "执行测试用例06"
