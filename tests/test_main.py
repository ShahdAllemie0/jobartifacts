import unittest
from src.main import add

class TestMain(unittest.TestMain):
    def test_add(self):
        self.asserEqual(add(1,2),3)

     
if __name__ == '__main__':
    unittest.main()     