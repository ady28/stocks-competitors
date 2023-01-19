from pymongo import MongoClient


def insert_competitors(ticker, competitors, database_data, environ_data):
    CONNECTION_STRING = f"mongodb://{database_data['MONGO_USER']}:{database_data['MONGO_PASS']}@{environ_data['MONGO_NAME']}:{environ_data['MONGO_PORT']}/{environ_data['MONGO_DB']}?authSource=admin"

    filter = {'ticker': ticker}
    new_value = {"$set": {'competitors': competitors}}

    try:
        mongo_client = MongoClient(CONNECTION_STRING)
    except Exception as msg:
        raise BaseException(f"{msg}")
    else:
        stocks_db = mongo_client["stocks"]
        stocks_collection = stocks_db["stocks"]
        try:
            stocks_collection.update_one(filter, new_value)
        except Exception as msg:
            raise BaseException(f"{msg}")
