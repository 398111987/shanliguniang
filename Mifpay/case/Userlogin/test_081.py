#coding:utf-8
import ddt
import unittest

testData = [{"username":"selenium","psw":"1111111"},
            {"username":"python","psw":"222222"},
            {"username":"appium","psw":"333333"}]
@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        print "end!"
    @ddt.data(*testData)
    def test_ddt(self,data):
        print data
if __name__ =="__main__":
    unittest.main()