import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = '6202160443:AAEaFi5CCq1OzkFfnBIEIzN58jOxCHb3Q9Y'
# TEXT: str = 'Ура! Классный апдейт!'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER: int = 100

updates: dict
timeout: int = 60
offset: int = -2
counter: int = 0
chat_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:
    start_time = time.time()
    print('attemp = ', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

    time.sleep(1)
    counter += 1

'''
respone = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
if respone.status_code == 200:   # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(respone.text)
else:
    print(respone.status_code)   # При другом коде ответа выводим этот код
'''
