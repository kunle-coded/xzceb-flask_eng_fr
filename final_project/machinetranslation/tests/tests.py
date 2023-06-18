import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase):

    def test1(self):
        self.assertEqual(translator.english_to_french("Hallo"), "Hello")

    def test2(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")


unittest.main()