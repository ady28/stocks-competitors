from dotenv import dotenv_values
import os


def get_environment():
    stocks_env = os.environ.get("STOCKS_APP_ENV")
    if stocks_env == None:
        stocks_env = "dev"
    return stocks_env


def get_env_data(stocks_env):
    e_data = {}
    if stocks_env == "dev":
        e_data = dotenv_values(".env-public")
    else:
        e_data['PORT'] = os.environ.get("PORT")
        e_data['MONGO_PORT'] = os.environ.get("MONGO_PORT")
        e_data['MONGO_NAME'] = os.environ.get("MONGO_NAME")
        e_data['MONGO_DB'] = os.environ.get("MONGO_DB")
    return e_data


def get_db_data(stocks_env):
    db_data = {}
    if stocks_env == "dev":
        db_data = dotenv_values(".env-secret")
    else:
        file = open("/run/secrets/stocksmongouser")
        db_data['MONGO_USER'] = file.read()
        file = open("/run/secrets/stocksmongopassword")
        db_data['MONGO_PASS'] = file.read()

        db_data['MONGO_USER'] = db_data['MONGO_USER'].strip()
        db_data['MONGO_PASS'] = db_data['MONGO_PASS'] .strip()
    return db_data
