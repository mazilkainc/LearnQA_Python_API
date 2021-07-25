import requests
import json
import time
import random

def get(token, time_wait):

    time.sleep(time_wait)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
    obj_json = json.loads(response.text)
    return obj_json

try:
#  1. Создание задачи
    response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    obj_json1 = json.loads(response1.text)
    token = obj_json1['token']
    timer = obj_json1['seconds']

#  3. Ожидания вынесены в функцию get (состоят из запроса внутри интервала ожидания и после завершения)
    time_1 = random.randint(0, timer-1)
    time_2 = timer - time_1

    print(f"Для {token} создана задача, подождите {time_1} сек до проверки и {timer} секунд до получения результата")
#  2. Один запрос до того как задача готова
#    token = "dasdfdsf"
#   неверный токен для проверки
    obj_json = get(token, time_1)
    if "status" in obj_json.keys():
        if obj_json["status"] == "Job is NOT ready":
            print(f"Прошло {time_1} сек, \"{obj_json['status']}\"")
#  4. Запрос после того как задача должна быть готова
            obj_json = get(token, time_2)
            if obj_json['status'] == "Job is ready" and obj_json['result'] != None:
                print(f"Прошло {timer} сек, \"{obj_json['status']}\" с результатом \"{obj_json['result']}\"")
            else:
                print("Что-то пошло не так")
        elif obj_json["status"] == "Job is ready" and obj_json['result'] != None:
            print(f"Таймер был слишком мал {timer}, \"{obj_json['status']}\" с результатом \"{obj_json['result']}\"")
    elif obj_json["error"] == "No job linked to this token":
        print(f"Неверный token = {token}, для него не была создана задача")
    else:
        print("Что-то пошло не так")

except Error as error:
    print(error)




