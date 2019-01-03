from flask import Flask, jsonify, request, json


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"status": 201, "message": "hi welcome to ireporter"})