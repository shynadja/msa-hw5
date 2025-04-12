import requests

# Хранит текст страницы в кэше
cached_text = None

def get_text(url):
    """Получение текста страницы."""
    global cached_text
    if cached_text is None:
        response = requests.get(url)
        cached_text = response.text
    return cached_text

def count_word_frequencies(text, word):
    """Подсчет частоты слова в тексте."""
    words = text.split()
    return words.count(word)

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # Читаем слова из файла
    with open(words_file, 'r') as file:
        words_to_count = [word.strip() for word in file.readlines() if word.strip()]

    # Получаем текст страницы
    text = get_text(url)

    # Подсчет частот слов
    frequencies = {word: count_word_frequencies(text, word) for word in words_to_count}
    
    print(frequencies)

if __name__ == "__main__":
    main()