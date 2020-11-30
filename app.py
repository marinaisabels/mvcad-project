from flask import Flask
from flask_restful import Resource, Api

from pessoa_pyco import retorna_pessoas

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas


#api.add_resource(HelloWord, "/")
api.add_resource(Pessoa, "/pessoas")

if __name__ == "__main__":
    app.run(debug=True)
