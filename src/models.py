from pydantic import BaseModel, Field
from enums import FiatCurrency, CryptoCurrency


class TransactionReceiptRequest(BaseModel):
    tx_hash: str = Field(..., alias='txhash')


class GetRevenueFromTaskResponse(BaseModel):
    income: dict[FiatCurrency | CryptoCurrency, str]
