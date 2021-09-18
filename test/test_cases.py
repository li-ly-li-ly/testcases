import unittest
import logging
logging.basicConfig(level=logging.INFO)
class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logging.info('setipcalsss')
    @classmethod
    def tearDownClass(cls) -> None:
        logging.info('trear down class')
    def setUp(self) -> None:
        logging.info('开始')
    def tearDown(self) -> None:
        logging.info('结束')
    def test_01(self):
        logging.info('第一个测试用例执行')
        self.assertEqual(1,2,'判断相等')

    def test_02(self):
        logging.info('第一个测试用例执行')
        self.assertEqual(2, 2, '判断相等')
    @unittest.skip
    def test_03(self):
        logging.info('第一个测试用例执行1')
        self.assertEqual(2, 5, '判断相等')
if __name__ == '__main__':
    unittest.main()