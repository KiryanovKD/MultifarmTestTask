from dataclasses import dataclass
import os


@dataclass
class BlockchainDataExtractionAppConfig:
    ETHERSCAN_API_KEY: str = os.environ.get('ETHERSCAN_API_KEY', 'YourApiKeyToken')

    HOST: str = '0.0.0.0'
    PORT: int = 8080


conf: BlockchainDataExtractionAppConfig = BlockchainDataExtractionAppConfig()
