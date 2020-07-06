from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
import json
import requests


#essas primeiras duas linhas são necessárias para puxar o que foi importado acima
app = Flask(__name__)
api = Api(app)

@app.route('/')
def pag_inicial():
    return render_template('pag_inicial.html')


@app.route('/resultado/', methods=['GET', 'POST'])
def dados_pkm():
    x = request.form['insere_num']
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(x))
    dados = response.json()

    for i in dados['forms']:
        nome_pkm = 'Nome: {}'.format(i['name'].upper())

    lista = []
    for i in dados['types']:
        tipo_pkm = 'Tipo: {}'.format(i['type']['name'].upper())
        #print(i)
        s = ''
        print(s.join(i['type']['name']))
    # s = ''
    # print(s.join(i['type']['name']))

    for i in dados['abilities']:
        golpes_pkm = 'Golpe: {}'.format(i['ability']['name'].upper())

    for i in dados['stats']:
        stats_pkm = 'Stat: {}'.format(i['stat']['name'].upper())



    altura = dados['height']
    altura_m = altura / 10
    altura_pkm = 'Altura: {} m'.format(altura_m)

    peso = dados['weight']
    peso_kg = peso / 10
    peso_pkm = 'Peso: {} kg'.format(peso_kg)

    foto_pkm = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{}.png'.format(x)

    return render_template('resultado.html',
                                nome_pkm=nome_pkm,
                                    tipo_pkm=tipo_pkm,
                               golpes_pkm=golpes_pkm,
                               stats_pkm=stats_pkm,
                                altura_pkm=altura_pkm,
                                peso_pkm=peso_pkm,
                                foto_pkm=foto_pkm)


if __name__ == '__main__':
     app.run(debug=True)