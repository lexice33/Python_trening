import requests

event_types = ['catalogue',
               'basket_transition',
               'basket_add',
               'checkout',
               'order_m',
               'thank_you_page',
               'authorisation',
               'uninstall',
               'server_busy',
               'feedback_add',
               'registration'
               ]

devices = ['ios', 'android']

when = ['today_data', 'yesterday_data']

# yesterday_data = f'http://188.227.16.46/api/yesterday_data?eventType=checkout&device=ios'
# today_data = 'http://188.227.16.46/api/today_data?eventType=catalogue&device=android'

yesterday_data = f'http://188.227.16.46/api/{when}?eventType={event_types}&device={devices}'
today_data = f'http://188.227.16.46/api/today_data?eventType=catalogue&device=android'

event = 0
date_vi = 0

# for i in range(len(event_types)):
#     req = requests.get(f'http://188.227.16.46/api/yesterday_data?eventType={event_types[event]}&device=ios').json()
#     event = event + 1
#     for on in range(len(when)):
#         req_one = requests.get(f'http://188.227.16.46/api/{when[date_vi]}?eventType={event_types[event]}&device=ios').json
#         date_vi = date_vi + 1

for i in range(len(event_types)):
    req = requests.get(f'http://188.227.16.46/api/yesterday_data?eventType={event_types[event]}&device=ios')
    if req.json()["total_count"] > 0:
        print(f'IOS: Ивент {event_types[event]} за ВЧЕРА работает')
    elif req.json()["total_count"] == 0:
        print(f'IOS: Ивент {event_types[event]} за ВЧЕРА имеет нулевое значение')
    elif req.status_code != 200:
        print(f'IOS: Ивент {event_types[event]} за ВЧЕРА имеет код ответа {req.status_code}')
    event = event + 1

print()
print()

event = 0


for aa in range(len(event_types)):
    req = requests.get(f'http://188.227.16.46/api/yesterday_data?eventType={event_types[event]}&device=android')
    if req.json()["total_count"] > 0:
        print(f'Android: Ивент {event_types[event]} за ВЧЕРА работает')
    elif req.json()["total_count"] == 0:
        print(f'Android: Ивент {event_types[event]} за ВЧЕРА имеет нулевое значение')
    elif req.status_code != 200:
        print(f'Android: Ивент {event_types[event]} за ВЧЕРА имеет код ответа {req.status_code}')
    event = event + 1

print()
print()

event = 0


for i in range(len(event_types)):
    req = requests.get(f'http://188.227.16.46/api/today_data?eventType={event_types[event]}&device=ios')
    if req.json()["total_count"] > 0:
        print(f'IOS: Ивент {event_types[event]} за СЕГОДНЯ работает')
    elif req.json()["total_count"] == 0:
        print(f'IOS: Ивент {event_types[event]} за СЕГОДНЯ имеет нулевое значение')
    elif req.status_code != 200:
        print(f'IOS: Ивент {event_types[event]} за СЕГОДНЯ имеет код ответа {req.status_code}')
    event = event + 1
print()
print()

event = 0


for i in range(len(event_types)):
    req = requests.get(f'http://188.227.16.46/api/today_data?eventType={event_types[event]}&device=android')
    if req.json()["total_count"] > 0:
        print(f'Android: Ивент {event_types[event]} за СЕГОДНЯ работает')
    elif req.json()["total_count"] == 0:
        print(f'Android: Ивент {event_types[event]} за СЕГОДНЯ имеет нулевое значение')
    elif req.status_code != 200:
        print(f'Android: Ивент {event_types[event]} за СЕГОДНЯ имеет код ответа {req.status_code}')
    event = event + 1
print()
print()


