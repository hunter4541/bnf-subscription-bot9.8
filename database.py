from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client['bnf_bot']

users_col = db['users']
channels_col = db['channels']
payments_col = db['payments']
admins_col = db['admins']

users_col.create_index("user_id")
channels_col.create_index("channel_id")
payments_col.create_index("utr", unique=True)
