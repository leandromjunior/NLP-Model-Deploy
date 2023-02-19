import json
from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)

@app.route("/")

#Verificando se um parâmetro foi enviado para o modelo
def index():
    if "query" not in request.args:
        return jsonify({"prediction" : None, "message" : "send me a text"})

    query = request.args.get("query")
    model = load("model.joblib")
    labels = ['carros', 'economia', 'educacao', 'esporte', 'musica', 'politica']

    predict = model.predict([query])
    prediction = labels[predict[0]]

    return jsonify({"A categoria desta manchete é" : prediction})