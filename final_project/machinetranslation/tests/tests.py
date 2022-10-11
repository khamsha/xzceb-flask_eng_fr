import unittest

from translator import englishToFrench, frenchToEnglish

class TestEng2Fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(' '), ' ') # test for null input
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test translation of 'Hello' to French
        

class TestFr2Eng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(' '), ' ') # test for null input
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test translation of 'Bonjour' to English
        
unittest.main()