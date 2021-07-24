import requests

try:
    response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
    if response.status_code == 200:
        print(f"Конечный URL: {response.history[len(response.history)-1].url}")
        print(f"Переходов до {response.history[len(response.history)-1].url}: {len(response.history)}")
        print(f"Всего переходов: {(len(response.history))+1}")
    else:
        print(f"Что-то пошло не так, code: {response.status_code}")
except Error as error:
    print(error)