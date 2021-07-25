import requests
methods = ["GET", "POST", "PUT", "DELETE", "HEAD", ""]


try:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print("1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.",
          f"-Выводит \"{response.text}\"", sep="\n")
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{methods[5]}"})
    print("2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.",
          f"-Выводит \"{response.text}\"", sep="\n")
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",
                            params={"method":"GET"})
    print("3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае",
          f"-Выводит \"{response.text}\"", sep="\n")
    print("4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. "
          "Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ "
          "и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип "
          "запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.")
    for i in range(0, len(methods)):
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":f"{methods[i]}"})
        if response.text == '{"success":"!"}':
            print(f"get сработал с параметрами \"method\":\"{methods[i]}\"")
    for type in (requests.post, requests.put, requests.delete):
        for i in range(0, len(methods)):
            response = type("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                    data={"method": f"{methods[i]}"})
            if response.text == '{"success":"!"}':
                print(f"{type.__name__} сработал с body \"method\":\"{methods[i]}\"")

except Error as error:
    print(error)