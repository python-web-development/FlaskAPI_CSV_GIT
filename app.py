from flask import Flask, render_template
import pandas as pd
# from redoc import Redoc


app = Flask(__name__)
# redoc = Redoc(app, serve_spec=False)

@app.route('/')
def home():
    a = "Hello World"
    return(a)

@app.route('/walmart')
def data_walmart():
    df1 = pd.read_csv("Walmart-data.csv")
    df = df1.to_dict(orient='records')  # convert dataframe to
    print(df)
    return(df)


@app.route('/onlinefoods' , methods = ['GET'])
def onlinefoods():
    df2 = pd.read_csv("onlinefoods.csv")
    df = df2.to_dict(orient='records')  # convert dataframe to
    print(df)
    return(df)

# @app.route('/docs')
# def docs():
#     return send_file('swagger.json')

# @app.route('/redoc')
# def redoc_ui():
#     return redoc.to_dict()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)