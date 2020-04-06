import unittest
import time
from config.setting import logging

class StartEnd(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):


    def setUp(self):
        logging.info("-----------------------------------------------")
        logging.info("本轮用例开始执行")



    def tearDown(self):
        self._testMethodName = self._testname
        self._testMethodDoc =self._testid
        logging.info("本轮用例执行完毕，开始下一条用例")
        # logging.info("---------------------------------------------------")


    # @classmethod
    # def tearDownClass(cls):
    #     logging.info("---------------------------------------------------")
