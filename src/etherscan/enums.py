from enum import Enum


class Module(str, Enum):
    PROXY = 'proxy'


class Action(str, Enum):
    GET_TRANSACTION_RECEIPT = 'eth_getTransactionReceipt'
