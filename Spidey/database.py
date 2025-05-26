# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

from pymongo import MongoClient
from configs import * #

client = MongoClient(Spidey.DATABASE_URI)

users = client['main']['users']
groups = client['main']['groups']

def already_db(user_id):
    user = users.find_one({"user_id": str(user_id)})
    return bool(user)

def already_dbg(chat_id):
    group = groups.find_one({"chat_id": str(chat_id)})
    return bool(group)

def add_user(user_id, name):
    if already_db(user_id):
        return
    users.insert_one({"user_id": str(user_id), "name": name, "ban_status": {"is_banned": False}})

def remove_user(user_id):
    if not already_db(user_id):
        return
    users.delete_one({"user_id": str(user_id)})

def add_group(chat_id):
    if already_dbg(chat_id):
        return
    groups.insert_one({"chat_id": str(chat_id)})

def all_users():
    return users.count_documents({})

def all_groups():
    return groups.count_documents({})

def get_all_users():
    return list(users.find({}, {"user_id": 1, "name": 1, "_id": 0}))
    
def add_user(user_id, name):
    if already_db(user_id):
        users.update_one({"user_id": str(user_id)}, {"$set": {"name": name}})
        return
    users.insert_one({"user_id": str(user_id), "name": name, "ban_status": {"is_banned": False}})
    
def already_db(user_id):
    """Checks if the user is already in the MongoDB database"""
    return users.find_one({"user_id": str(user_id)}) is not None
        
# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777     
