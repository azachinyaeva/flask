import requests


response = requests.post(
    'http://127.0.0.1:5000/adv/',
    json={'title': 'test', 'description': 'test_adv_description', 'user': 'test_user'}
)
print(response.status_code)
print(response.text)


response = requests.get(
    'http://127.0.0.1:5000/adv/1/'
)
print(response.status_code)
print(response.text)


response = requests.delete('http://127.0.0.1:5000/adv/1/')
print(response.status_code)
print(response.text)
