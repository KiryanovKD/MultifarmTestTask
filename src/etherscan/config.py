from dataclasses import dataclass


@dataclass
class EtherscanConfig:
    API_URL: str = 'https://api.etherscan.io'


etherscan_conf = EtherscanConfig()
