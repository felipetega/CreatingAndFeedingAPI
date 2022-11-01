import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# construir funcionalidades


@app.route("/")
def homepage():
    return "Essa é a homepage do site"


@app.route("/vendas")
def vendas():
    tabela = pd.read_excel("dados.xlsx")
    total_vendas = tabela["Vendas"].sum()
    print(total_vendas)
    resposta = {"total_vendas": total_vendas}
    return jsonify(resposta)


# rodas nossa api
# app.run(host="0.0.0.0")
app.run()
