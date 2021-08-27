import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MTMyYTExYjgtNzE4OS00NDc2LWI3NmItNmY1NGMwNzNlNzQ5OjZlOTg4MDJkNmRlMDQ2ZmE5ZGM2YjcyOWM3NWM4OWE1'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text

while True:
     word = input('Введите слово для перевода: ')
     if word:
         hearders_translate = {'Authorization': 'Bearer ' + token}
         params = {'text': word, 'srcLang': 1033, 'dstLang': 1049}
         r = requests.get(URL_TRANSLATE, headers=hearders_translate, params=params)
         res = r.json()
         try:
             print(res['Translation']['Translation'])
         except:
             print('Не найдено варианта для перевода')
         else:
             print('Готово')