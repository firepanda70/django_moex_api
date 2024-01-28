from dataclasses import dataclass
from datetime import datetime

import requests


USD_RUB_RATE_URL = (
    'http://iss.moex.com/iss/engines/currency/markets/'
    'selt/boards/CETS/securities/USD000UTSTOM.json'
)


class MOEXClinetException(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(f'Fail on rate request: {reason}')


@dataclass
class RateResponse:
    rate: float
    request_datetime: datetime


class MOEXClient:
    def __init__(self):
        self.__history: list[RateResponse] = []
    
    def __update_history(self, rate: RateResponse):
        self.__history.append(rate)
        if len(self.__history) > 10:
            self.__history.pop(0)
    
    def get_history(self):
        return self.__history

    def get_usd_rub_rate(self):
        try:
            response = requests.get(USD_RUB_RATE_URL)
            data = response.json()
        except Exception as e:
            raise MOEXClinetException(e)
        rate = RateResponse(
            data['marketdata']['data'][0][8],
            datetime.now()
        )
        self.__update_history(rate)
        return rate


moex_client = MOEXClient()
