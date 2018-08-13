# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print "end!"
    def test08(self):
        print "执行测试用例08"
    def test09(self):
        print "执行测试用例09"
    def test10(self):
        print "执行测试用例10"
