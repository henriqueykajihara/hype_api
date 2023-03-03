from flask import Flask, make_response, jsonify, request
from calculo_output import calcula
from bd import Medicoes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

"""
Não entendi muito bem o exercício para poder criar um banco de dados para ele. Um
medidor de batimentos cardíacos gera inúmeras informações por minuto, então como isso
seria guardado neste banco e para quais fins?
"""

@app.route('/medicoes', methods=['POST'])
def post_medicoes():
    """
        Neste ponto seria validado as informações do post e estas seriam gravadas 
        num banco
    """
    Medicoes.append(request.json)
    return make_response(
        jsonify(mensagem='Medições cadastradas', dados=Medicoes)
    )

@app.route('/calculo', methods=['GET'])
def get_calculo():

    """
        Retorna os batimentos cardíacos já calculados
    """
    return make_response(
        jsonify(calcula(Medicoes()))
    )

"""
def get_token():
    return


def new_client():
    return
"""

if __name__ == '__main__':
    app.run()
