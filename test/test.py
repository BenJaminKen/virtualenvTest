import unittest

#当测试开始后，flask会自动创建TestClass对象
# 然后调用setUp，然后调用我们自己写的方法，最后调用tearDown
class TestClass(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass