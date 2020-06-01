import unittest

import HTMLTestRunner

import testfile

class fileTest(unittest.TestCase):

    @classmethod

    def setUpClass(self):

        pass

    @classmethod

    def tearDownClass(self):

        pass

    def setUp(self):

        pass

    def tearDown(self):

        pass

    def test_jg(self):

        print('test_jg:')

        rv = testfile.szys()

        assert  0 <= rv <= 100    #测试题目结果是否在0到100以内


    def test_zs(self):

        print('test_zs:')

        rv = testfile.szys()

        self.assertIsInstance(rv,int)  #测试题目答案是否是整数


    def test_k(self):

        print('test_k:')

        rv = testfile.szys()

        self.assertIsNotNone(rv)    #测试函数返回值是否为空


    def test_n(self):

        print('test_n:')

        rv = testfile.szys()

        self.assertEqual(rv,10)     #测试函数返回值为具体某数，因为题目是随机产生，所以本条测试在大部分测试下都应不通过


if __name__ == '__main__':

        suite = unittest.TestSuite()

        suite.addTest(fileTest("test_jg"))

        suite.addTest(fileTest("test_zs"))

        suite.addTest(fileTest("test_k"))

        suite.addTest(fileTest("test_n"))
