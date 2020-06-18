from flask import Flask 
from kubernetes import client,config

app=Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")