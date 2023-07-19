# --------------------- inglizcha -> o'zbekcha tarjimon ----------------------------
import inflect
from googletrans import Translator


# функция для преобразования чисел в слова
def num2words(num):
    p = inflect.engine()
    word = p.number_to_words(num)
    return str(word)


# print(num2words(23))


# Функция, переводящая слова, преобразованные с помощью функции num2words, с английского языка на узбекский.
def eng2uzb(phrase):
    translator = Translator()
    translated = translator.translate(phrase, src='en', dest='uz')
    return translated.text

# print(eng2uzb(num2words(4)))
