import os

import requests
from datetime import datetime, timedelta


APP_ID = os.environ.get('OXR_APP_ID')
URL = 'http://openexchangerates.org/api/latest.json?app_id={}'.format(APP_ID)

last_request_time = datetime.now()
hour = timedelta(hours=1)
last_response = requests.get(URL).json()['rates']


def rates():
    global last_request_time, hour, last_response

    if last_request_time + hour < datetime.now():
        last_response = requests.get(URL).json()['rates']
        last_request_time = datetime.now()

    return last_response


def dollar(currency, amount):
    return amount/rates()[currency]
