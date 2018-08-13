# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "start!"

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print"end!"

    def test01(self):
        print"case01"

    def test03(self):
        print "case03"

    def test02(self):
        print "case02"

    def addtest(self):
        print "add test"

if __name__ =="__main__":
    unittest.main()
