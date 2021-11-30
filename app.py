import json
from werkzeug.security import generate_password_hash

import jwt
from flask import Flask
from flask_restful import Resource, Api, request
from models import Pessoas
from flask.json import jsonify

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, id):
        try:
            pessoa = Pessoas.query.filter_by(id=id).first()
            response = {
                'nome': pessoa.nome,
                'id': pessoa.id
            }
            return response
        except:
            return { 'erro': 'Nenhum usuario identificado com o id informado.'}

class Usuarios(Resource):
    # def get(self):
    #     pessoas = Pessoas.query.all()
    #     return pessoas
    def post(self):
        pessoa = Pessoas(nome='Desmennyellysson', idade=30)
        pessoa.save()

class Auth(Resource):
    def post(self):
        try:
            key = "senhaSuperSecretaESegura"
            user = json.loads(request.data)
            pass_hash = generate_password_hash(user["pass"])
            payload = {
                "user": "Desmennyellysson Jerry",
                "login": user['login'],
                "level": 5
            }
            jwtToken = jwt.encode(payload, key, algorithm="HS256")
            response = {
                "jwt-token": jwtToken
            }
            return response
        except:
            return {"error": "Bad request"}

    def get(self):
        try:
            token = request.headers.get('authorization')
            payload = jwt.decode(token, "senhaSuperSecretaESegura", algorithms=["HS256"])
            return {"status": "ok", "payload": payload}
        except:
            return {"error": "deu ruim"}

api.add_resource(Pessoa, '/pessoas/<int:id>')
api.add_resource(Usuarios, '/pessoas')
api.add_resource(Auth, '/signin')

if __name__ == '__main__':
    app.run(debug=True)