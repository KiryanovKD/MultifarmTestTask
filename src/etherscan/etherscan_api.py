import aiohttp
import logging
from typing import Any

from .config import etherscan_conf
from .models.transaction import TransactionReceipt
from .enums import Module, Action


def kwargs_to_request_params(**kwargs: str) -> str:
    return '&' + '&'.join([f'{k}={v}' for k, v in kwargs.items()])


class EtherscanAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def __request(self, module: Module, action: Action, **kwargs: str) -> dict[str, Any]:
        req = f'{etherscan_conf.API_URL}/api?module={module}&action={action}&apikey={self.api_key}'
        additional_params = kwargs_to_request_params(**kwargs)
        req += additional_params

        async with aiohttp.ClientSession() as session:
            async with session.get(req) as resp:
                return (await resp.json())['result']  # type: ignore

    async def get_transaction_receipt(self, txhash: str) -> TransactionReceipt | None:
        module = Module.PROXY
        action = Action.GET_TRANSACTION_RECEIPT

        try:
            result = await self.__request(module, action, txhash=txhash)
            return TransactionReceipt(**result)
        except Exception as e:
            logging.error(f'Error in get_transaction_receipt! {str(e)}')
            return None
