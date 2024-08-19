#_*_coding:utf-8_*_
#author     :lenovo
#time       :2020/5/29 9:22
#file       :static.py
#IDE        :PyCharm
# static.py
import unittest
import HTMLTestRunner
import yunsuan
import random

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        print("execute tearDownClass")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    def test_limit(self):
        print('execute test_limit')
        t = yunsuan.sarithmeticzys()
        assert 0 < t < 100

    def test_negative(self):
        print('execute test_negative')
        t = yunsuan.arithmetic()
        t = -1

    def test_than(self):
        print('execute test_than')
        t = yunsuan.arithmetic()
        assert t > 100

    def test_empty(self):
        print('execute test_empty')
        t = yunsuan.arithmetic()
        self.assertIsNotNone(t)

    def test_integer(self):
        print('execute test_integer')
        t = yunsuan.arithmetic()
        self.assertIsInstance(t, int)

    def test_test(self):
        print('execute test_test')
        m = yunsuan.test()


if __name__ == '__main__':
        suite = unittest.TestSuite()
        # Test是要测试的类名，test_one是要执行的测试方法
        suite.addTest(Test("test_limit"))
        suite.addTest(Test("test_negative"))
        suite.addTest(Test("test_than"))
        suite.addTest(Test("test_empty"))
        suite.addTest(Test("test_integer"))
        suite.addTest(Test("test_test"))
        # 实践中发现执行时的当前路径，不一定是此文件所在的文件夹，所以使用绝对路径
        # print(f"{os.getcwd()}")
        filename = 'D:\\apptestresult.html'
        fb = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title="测试HTMLTestRunner", description="测试HTMLTestRunner")
        runner.run(suite)
        fb.close()
