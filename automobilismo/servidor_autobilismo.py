from flask import Flask, json, jsonify
from flask import request
from classes import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "Campeonato de pilotos; <a href=/Camp_Pilotos> listar o campeonato</a>"

@app.route('/Camp_pilotos')
def listar():
    campeonato = list(map(model_to_dict, Campeonato.select()))
    response = jsonify({"lista": campeonato})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True, port=4999)