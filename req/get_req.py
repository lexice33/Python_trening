import requests
import uuid
url = 'https://api.leroymerlin.ru/mobile/'
auth_by_pass = 'user/authByPassword?'
login_get = 'login=antif+1'
pass_get = 'password=Antif83'
headers = {'apikey': 'NLdu-FEUbU-CCrd-otTWYJGhDfZZKYHAxVd-QksZEMMtCUkUKk'}
url_auth_by_pass = url + auth_by_pass + login_get + '&' + pass_get
# print(str(url_auth_by_pass))

req_auth = requests.get(url_auth_by_pass, headers=headers)

# print(req_auth.status_code)
# print(req_auth.json()['data']['Not authorize'])

# def req_auth_1():
#     req_auth.

# def test_123():
#     req_po = req_auth.json()['errors']
#     assert req_auth.status_code == 200, 'Status code ' + str(req_auth.status_code) + \
#                                         ' вместо 200. ' + 'Ошибка: ' + str(req_po)
#
# test_123()

# req_po = req_auth.json()
# req_po1 = req_po['errors']
#
# print(req_po1)

# list.append()
u = uuid.uuid1()

print(u)
ee = []

