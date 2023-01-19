import stock_comp
import env_data
import stocks_db
from flask import Flask, jsonify, request

app = Flask(__name__)

stocks_env = env_data.get_environment()
environ_data = env_data.get_env_data(stocks_env)
database_data = env_data.get_db_data(stocks_env)


@app.route('/competitors', methods=["GET"])
def competitors():
    ticker = request.args.get('ticker').upper()
    exchange = request.args.get('exchange').upper()

    ret = {
        "success": False,
        "message": ""
    }

    try:
        competitor_list = stock_comp.get_competitors(ticker=ticker, exchange=exchange)
    except BaseException as msg:
        ret['message'] = f"There was an error getting stock competitor data data: {msg}"
    else:
        try:
            stocks_db.insert_competitors(ticker=ticker, competitors=competitor_list, database_data=database_data, environ_data=environ_data)
        except BaseException as msg:
            ret['message'] = f"There was an error updating the stock: {msg}"
        else:
            ret['message'] = "The competitors list has been updated"
            ret['success'] = True

    return jsonify(ret)


if __name__ == "__main__":
    if stocks_env != "dev":
        from waitress import serve
        serve(app, host="0.0.0.0", port=environ_data["PORT"])
    else:
        app.run(debug=True, port=environ_data["PORT"])
