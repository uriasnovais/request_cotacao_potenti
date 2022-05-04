from request import get_dicio
from flask import Flask, jsonify
import datetime
from time import sleep


dados = get_dicio()

hoje = datetime.datetime.now()

"""for chave, valor in dados.items():
  print(chave)
  for chave_2, valor_2 in dados[chave].items():
    print(f'{chave_2}: {valor_2}\n')"""

app = Flask(__name__)

#construir funções
@app.route('/')
def homepage():
  return f'A Api está Funcional \nUltima Atualização {hoje}'

@app.route('/pegar-ct')
def pegarvendas():
  return jsonify(dados)

#rodar api
def run():
  while True:
    app.run(host= '0.0.0.0')
    sleep(30)

run()