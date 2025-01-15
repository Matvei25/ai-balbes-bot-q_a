# Обязательно укажите local_context
#
# !!!

import logging
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Создаем пайплайн для задачи "вопрос-ответ"
qa_pipeline = pipeline("question-answering")

def ask_question(context: str, question: str) -> str:
    # Используем пайплайн для получения ответа
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def search_internet(query: str) -> str:
    # Пример простого поиска информации в интернете
    search_url = f"https://www.google.com/search?q={query}"
    
    # Выполняем GET-запрос к Google (или другому поисковику)
    response = requests.get(search_url)
    
    # Используем BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Извлекаем текст из результатов поиска (это может быть изменено в зависимости от структуры страницы)
    results = soup.find_all('h3')
    
    # Собираем текст из первых нескольких заголовков
    context = "\n".join([result.get_text() for result in results[:3]])
    
    return context if context else "Не удалось найти информацию."

def main():
    while True:
        user_query = input("Введите ваш вопрос (или 'exit' для выхода): ")
        if user_query.lower() == 'exit':
            break
        
        # Получаем дополнительный контекст из интернета
        internet_context = search_internet(user_query)

        # Пример контекста (можно расширить или изменить)
        local_context = """"""  # Добавьте сюда свой локальный контекст
        
        # Объединяем контексты
        combined_context = local_context + "\n" + internet_context + "\n" + user_query

        # Получаем ответ на сообщение пользователя
        answer = ask_question(combined_context, user_query)
        
        # Выводим ответ
        print(f"Ответ: {answer}")

if __name__ == '__main__':
    main()