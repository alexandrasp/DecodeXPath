import webscrapper
import unittest

class TestWepscrapper(unittest.TestCase):
    
    def test_outputMessage_false(self):       
        result = webscrapper.outputMessage(False, 1)
        self.assertEqual(result, "ALERT - Can’t move to page 2: page 1 link has been malevolently tampered with!!")

if __name__ == '__main__':
    unittest.main()