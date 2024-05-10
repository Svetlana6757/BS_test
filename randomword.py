from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator


def get_english_world():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None

def translate_to_russian(word, definition):
    translator = GoogleTranslator(source='en', target='ru')
    word_translated = translator.translate(word)
    definition_translated = translator.translate(definition)
    return word_translated, definition_translated

# Игра "Угадай слово"
def word_game():
    print("Добро пожаловать в игру 'Угадай слово'")

    while True:
        word_dict = get_english_world()
        if word_dict is None:
            print("Не удалось получить слово, попробуйте снова.")
            continue

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Перевод слова и определения на русский язык
        word_russian, word_definition_russian = translate_to_russian(word, word_definition)

        print(f"Значение слова: {word_definition_russian} (по-английски: {word_definition})")
        user = input("Какое это слово? ")

        if user.lower() == word_russian.lower():
            print("Вы угадали!")
        else:
            print(f"Ответ неверный, было загадано слово - {word_russian} (по-английски: {word})")


        play_again = input("Хотите продолжить? Да/Нет").strip().upper()
        if play_again != "ДА":
            print("Спасибо за игру!")
            break

word_game()