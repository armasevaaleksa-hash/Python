import re
from collections import Counter

def find_word(text, word):
    return word.lower() in text.lower()


def replace_word(text, old, new):
    return text.replace(old, new)

def split_words(text):
    return text.split()



def analyze_text(text):
    words = re.findall(r"\b[\w'-]+\b", text.lower())


    main_text = text.split("Email для зв'язку:")[0]
    sentences = re.split(r"(?<=[.!?])\s+", main_text.strip())

    print(f"Кількість слів: {len(words)}")
    print("Кількість речень: {}".format(len(sentences)))

    frequency = Counter(words)

    print("\n10 найчастіших слів:")
    for word, count in frequency.most_common(10):
        print(f"{word} - {count}")

def find_keywords(text):
    keywords = [
        "NeoTerra",
        "квантові комп'ютери",
        "штучний інтелект",
        "технології",
        "майбутнє"
    ]

    print("\nКлючові слова та фрази:")
    for word in keywords:
        count = text.lower().count(word.lower())
        print(f"{word}: {count}")


def find_computers(text):
    return re.findall(r"\bQC-\d+\b", text)


def find_email(text):
    return re.findall(r"[\w.-]+@[\w.-]+\.[a-zA-Z]+", text)


try:
    with open("src/data/neoterra_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("АНАЛІЗ ТЕКСТУ NEOTERRA 3000\n")

    analyze_text(text)
    find_keywords(text)

    print("\nПошук слова NeoTerra:")
    print(find_word(text, "NeoTerra"))

    print("\nЗаміна слова:")
    print(replace_word("Привіт, NeoTerra!",
                       "NeoTerra", "Python"))

    print("\nМоделі квантових комп'ютерів:")
    print(find_computers(text))

    print("\nЗнайдені email:")
    print(find_email(text))

except FileNotFoundError:
    print("Помилка! Файл не знайдено.")

except Exception as error:
    print(f"Помилка: {error}")

