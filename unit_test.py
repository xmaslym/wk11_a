import unittest
from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_helloWorld(self):
        a = HelloWorld("Hello World!")
        self.assertEqual(a.msg, "Hello World!")

if __name__ == '__main__':
    unittest.main()
