import asyncio
import aioschedule as schedule
import time
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import time
from settings import (
    TYPE_WALLET
)
import ccxt
from loguru import logger
from module import *
from utils.gas_checker import get_gas, get_gas_starknet


URL_CONNECT_MONGO = ""
MONGO_DB = ""
COLLECTION_DATA_MONGO = ""
COLLECTION_HIST_MONGO = ""
COLLECTION_SETTINGS_MONGO = ""

mongoData = {
    
}
clientMongo = AsyncIOMotorClient(URL_CONNECT_MONGO, server_api=ServerApi('1'))
dbMongo = clientMongo[MONGO_DB]
collectionDataMongo = dbMongo[COLLECTION_DATA_MONGO]
collectionHistMongo = dbMongo[COLLECTION_HIST_MONGO]
collectionSettingsMongo = dbMongo[COLLECTION_SETTINGS_MONGO]

key = ''
recipient = ''


class StarkNetGasChecker():
    async def db_update(self, module_name, result_db):

        collectionDataMongo.update_many(
            {'module_name':module_name}, 
            {"$set":{
                'name':result_db.get('name'),
                'description':result_db.get('description'),
                'with_approve':result_db.get('with_approve'),
                'gas_status':result_db.get('gas_status'),
                'gas_eth':result_db.get('gas_eth'),
                'gas_usd':result_db.get('gas_usd'),
                'gas_time':result_db.get('gas_time'),
                'url':result_db.get('url'),
                }}, 
                upsert=True)

    async def form_result(self, module_name, data):
            
            module_name          = module_name
            name                 = ''
            description          = ''
            with_approve         = '0'
            gas_status           = 0
            gas_eth              = '-'
            gas_usd              = '-'
            gas_time             = time.time()
            url                  = ''

            name = data.get('name')
            description = data.get('description')
            with_approve = data.get('with_approve')
            gas_status = data.get('gas_status')

            gas_eth = data.get('gas_eth')
            if gas_eth == None:
                gas_eth = '-'

            if gas_eth != '-':
                gas_usd = float(gas_eth * self.eth_price)

            url = data.get('url')
            if url == None:
                url = ''
                
            return {
                'name':name,
                'description':description,
                'with_approve':with_approve,
                'gas_status':gas_status,
                'gas_eth':gas_eth,
                'gas_usd':gas_usd,
                'gas_time':gas_time,
                'url':url,
            }

    async def start_module(self, module_name):
        data = {}
        module_find = False

        for module_info in module_info_list:
            if module_info.get('module_name') == module_name:
                module = module_info.get('module')
                name = module_info.get('name')
                description = module_info.get('description')
                with_approve = module_info.get('with_approve')
                url = module_info.get('url')
                module_find = True
                break
        
        if module_find == False:
            return
        
        if module_name == A_make_transfer:
            gas_eth = await module('GAS', key, TYPE_WALLET, recipient)
        else:
            gas_eth = await module('GAS', key, TYPE_WALLET)

        if gas_eth == None:
            status = 0
        else:
            status = 1

        data.update({'name':name})
        data.update({'description':description})
        data.update({'with_approve':with_approve})
        data.update({'gas_eth':gas_eth})
        data.update({'gas_status':status})
        data.update({'url':url})
        result_db = await self.form_result(module_name, data,)
        await self.db_update(module_name, result_db)

    async def job(self):
        try:
            exchange = ccxt.binance()
            self.eth_price = exchange.fetch_ohlcv('ETH/USDT',limit=1)[0][3]
        except:
            return
        self.local_logger_dict = {}
        module_list = []
        module_list_find = collectionSettingsMongo.find({"do_back": "X"})
        module_list_find = await module_list_find.to_list(length=500)
        for module_find in module_list_find:
            module_list.append(module_find['module_name'])

        tasks = []
        for module in module_list:
                tasks.append(asyncio.create_task(self.start_module(module)))
        res = await asyncio.gather(*tasks)
        pass


async def job_check_gas():
    lo_appl = StarkNetGasChecker()
    task=[]
    await lo_appl.job()

async def start():
    schedule.every(3).seconds.do(job_check_gas)
    while True:
        await schedule.run_pending()
        time.sleep(0.1)
        
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    schedule.every(3).seconds.do(job_check_gas)
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)