from flask import Flask
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URL_CONNECT_MONGO = ""
MONGO_DB = ""
COLLECTION_DATA_MONGO = ""
COLLECTION_SETTINGS_MONGO = ""
COLLECTION_GAS_MONGO = ""

App = Flask(__name__)
App.json.sort_keys = False
cors = CORS(App) #modified
clientMongo = MongoClient(URL_CONNECT_MONGO, server_api=ServerApi('1'))
dbMongo = clientMongo[MONGO_DB]
collectionDataMongo = dbMongo[COLLECTION_DATA_MONGO]
collectionSettingsMongo = dbMongo[COLLECTION_SETTINGS_MONGO]
collectionGasMongo = dbMongo[COLLECTION_GAS_MONGO]