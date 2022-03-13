from pydantic import BaseModel, Field, validator


def hex_to_int(hex_value: str):
    return int(hex_value, base=0)


class TransactionLogEntity(BaseModel):
    address: str
    topics: list[str]
    data: int
    transaction_hash: str = Field(..., alias='transactionHash')
    transaction_index: int = Field(..., alias='transactionIndex')
    block_hash: str = Field(..., alias='blockHash')
    log_index: int = Field(..., alias='logIndex')
    removed: bool

    _cast_data = validator('data', pre=True, allow_reuse=True)(hex_to_int)
    _cast_transaction_index = validator('transaction_index', pre=True, allow_reuse=True)(hex_to_int)
    _cast_log_index = validator('log_index', pre=True, allow_reuse=True)(hex_to_int)


class TransactionReceipt(BaseModel):
    block_hash: str = Field(..., alias='blockHash')
    block_number: int = Field(..., alias='blockNumber')
    contract_address: str | None = Field(..., alias='contractAddress')
    cumulative_gas_used: int = Field(..., alias='cumulativeGasUsed')
    effective_gas_price: int = Field(..., alias='effectiveGasPrice')
    address_from: str = Field(..., alias='from')
    gas_used: int = Field(..., alias='gasUsed')
    logs: list[TransactionLogEntity]
    logs_bloom: str = Field(..., alias='logsBloom')
    status: int
    address_to: str = Field(..., alias='to')
    transaction_hash: str = Field(..., alias='transactionHash')
    transaction_index: int = Field(..., alias='transactionIndex')
    type: int

    _cast_block_number = validator('block_number', pre=True, allow_reuse=True)(hex_to_int)
    _cast_cumulative_gas_used = validator('cumulative_gas_used', pre=True, allow_reuse=True)(hex_to_int)
    _cast_effective_gas_price = validator('effective_gas_price', pre=True, allow_reuse=True)(hex_to_int)
    _cast_gas_used = validator('gas_used', pre=True, allow_reuse=True)(hex_to_int)
    _cast_status = validator('status', pre=True, allow_reuse=True)(hex_to_int)
    _cast_transaction_index = validator('transaction_index', pre=True, allow_reuse=True)(hex_to_int)
    _cast_type = validator('type', pre=True, allow_reuse=True)(hex_to_int)
