from enum import Enum


class FiatCurrency(str, Enum):
    USD = 'USD'


class CryptoCurrency(str, Enum):
    ETH = 'ETH'
