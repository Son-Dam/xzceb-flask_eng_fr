import unittest
from ...translator import frenchToEnglish, englishToFrench

class TestMyFunctions(unittest.TestCase):
    def test_englishToFrench_1(self):
        self.assertEqual(englishToFrench(None),None)
    def test_englishToFrench_2(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")  
    def test_englishToFrench_3(self):
        self.assertEqual(englishToFrench(''),'')  
    def test_frenchToEnglish_1(self):
        self.assertEqual(frenchToEnglish(None), None)
    def test_frenchToEnglish_2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test_frenchToEnglish_3(self):
        self.assertEqual(frenchToEnglish(''), '')    

if __name__ == '__main__':
    unittest.main()