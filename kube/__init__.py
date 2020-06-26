from flask import Flask,request,jsonify
from kubernetes import client,config

app=Flask(__name__)


from kube import routes