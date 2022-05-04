import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#construir funções
@app.route('/')
def homepage():
  return 'Essa é a home page'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

#rodar api
app.run(host= '0.0.0.0')
