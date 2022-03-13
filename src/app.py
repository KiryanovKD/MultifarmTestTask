import datetime

from config import conf
from etherscan import EtherscanAPI, TransactionReceipt

from models import TransactionReceiptRequest, GetRevenueFromTaskResponse
from utils import wei_to_eth
from enums import FiatCurrency, CryptoCurrency


class BlockchainDataExtractionApp:
    def __init__(self):
        self.etherscan_api = EtherscanAPI(api_key=conf.ETHERSCAN_API_KEY)

    async def get_transaction_receipt(self, tx_hash: str) -> TransactionReceipt | None:
        return await self.etherscan_api.get_transaction_receipt(txhash=tx_hash)

    async def get_revenue_from_task(self) -> GetRevenueFromTaskResponse:
        TX_HASH = '0x14dc5b46f607e2f0594bc633a50c1218f38f65216aaf3e9296f14bfa38fc3bc1'
        transaction_reciept = await self.etherscan_api.get_transaction_receipt(txhash=TX_HASH)
        revenue_in_wei = transaction_reciept.logs[1].data
        return GetRevenueFromTaskResponse(income={
            CryptoCurrency.ETH: wei_to_eth(revenue_in_wei)
        })
