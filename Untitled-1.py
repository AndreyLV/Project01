import requests

api_url = 'http://numbersapi.com/43'

respone = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
if respone.status_code == 200:   # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(respone.text)
else:
    print(respone.status_code)   # При другом коде ответа выводим этот код
