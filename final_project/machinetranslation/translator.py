'''Imports the deep_translator package'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Takes in a text and translates it to french'''

    french_text = MyMemoryTranslator(source= "english", target= "french").translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Takes in a french text and translates it to english'''

    english_text = MyMemoryTranslator(source= "french", target= "english").translate(french_text)
    return english_text
