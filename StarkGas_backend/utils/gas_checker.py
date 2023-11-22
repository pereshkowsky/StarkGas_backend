import time
import random

from starknet_py.net.gateway_client import GatewayClient

from web3 import Web3
from web3.eth import AsyncEth
from config import RPC
from settings import CHECK_GWEI, MAX_GWEI
from loguru import logger

from utils.sleeping import sleep


async def get_gas():
    try:
        w3 = Web3(
            Web3.AsyncHTTPProvider(random.choice(RPC["ethereum"]["rpc"])),
            modules={"eth": (AsyncEth,)},
        )
        gas_price = await w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')
        return gwei
    except Exception as error:
        logger.error(error)

async def get_gas_starknet():
    try:
        client = GatewayClient("mainnet")
        block_data = await client.get_block("latest")
        gas = Web3.from_wei(block_data.gas_price, "gwei")
        return gas
    except Exception as error:
        logger.error(error)
        
