import json
from json import JSONDecodeError

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
#json_text = 'text'

try:
    obj_json = json.loads(json_text)
    second_message = obj_json['messages'][1]['message']
    print(second_message)
except JSONDecodeError:
    print("Не Json")
except IndexError:
    print("Нет второго сообщения")