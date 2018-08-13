# coding:utf-8
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Test(unittest.TestCase):
    def test01(self):
        '''判断 a == b'''
        a = 1
        b = 1
        self.assertEqual(a,b)
    def test02(self):
        '''判断 a in b'''
        a ="hello"
        b ="hello world"
        self.assertIn(a,b)
    def test03(self):
        '''判断 a is True'''
        a = True
        self.assertTrue(a)

    def test04(self):

        a = "小丽"
        b = "lily"
        self.assertEqual(a,b,msg="失败原因：%s != %s"%(a,b))
if __name__ =="__main__":
    unittest.main()