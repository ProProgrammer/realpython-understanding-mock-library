from datetime import datetime

import requests


def is_weekday():
    today = datetime.today()

    # Python's datetime library treats Monday as 0 and Sunday as 6
    # So weekdays would be anything from 0 till 4 (4 included)
    return 0 <= today.weekday() < 5


def get_holidays():
    # print('get_holidays_called {}'.format(r))
    r = requests.get('http://localhost/api/holidays')
    print('get_holidays_called {}'.format(r))
    if r.status_code == 200:
        return r.json()
    return None
