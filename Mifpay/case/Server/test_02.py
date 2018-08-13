# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print "end!"
    def test11(self):
        print "执行测试用例11"
    def test12(self):
        print "执行测试用例12"
    def test13(self):
        print "执行测试用例13"
