import requests
import random
from time import sleep
from datetime import datetime

url = 'http://188.227.16.46/api/create_data'
event_types = [
    'catalogue',
    'basket_add',
    'basket_transition',
    'checkout',
    'order_m',
    'thank_you_page',
    'authorisation',
    'uninstall',
    'server_busy',
    'feedback_add',
    'registration'
]
success = [True, False]
users = range(100)
device = ['ios', 'android']


if __name__ == '__main__':
    for i in range(50000):
        user = random.choice(users)
        payload = {
            'userId': user,
            'eventType': random.choice(event_types),
            'success': random.choice(success),
            'timestamp': datetime.now().timestamp(),
            'device': random.choice(device)
        }
        requests.post(url, json=payload)
        print(f'Пользователь {user} выполнил запрос номер {i}')
        sleep(5)