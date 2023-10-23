import unittest
from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_helloWorld(self):
        a1 = HelloWorld("Hello World!")
        self.assertEqual(a1.msg, "Hello World!")
    def test_setMsg(self):
        a2 = HelloWorld()
        a2.setMsg("Hello World Everyone!")  
        self.assertEqual(a2.msg, "Hello World Everyone!")
    def test_featureX(self):
        a3 = HelloWorld()
        a3.featureX("HW Special!")
        self.assertEqual(a3.msg, "HW Special! featureX")

if __name__ == '__main__':
    unittest.main()
