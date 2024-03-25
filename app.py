from flask import Flask, render_template
import pandas as pd
import logging
# from redoc import Redoc



app = Flask(__name__)
# redoc = Redoc(app, serve_spec=False)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info("Root endpoint called")
    a = "Hello World"
    return(a)

@app.route('/walmart')
def data_walmart():
    logger.info("Item endpoint called with walmart data")
    df1 = pd.read_csv("Walmart-data.csv")
    df = df1.to_dict(orient='records')  # convert dataframe to
    # print(df)
    return(df)


@app.route('/onlinefoods' , methods = ['GET'])
def onlinefoods():
    logger.info(f"Item endpoint called with onlinefoods data")
    df2 = pd.read_csv("onlinefoods.csv")
    df = df2.to_dict(orient='records')  # convert dataframe to
    # print(df)
    return(df)

# @app.route('/docs')
# def docs():
#     return send_file('swagger.json')

# @app.route('/redoc')
# def redoc_ui():
#     return redoc.to_dict()

if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=5000)
    app.run(debug=True)