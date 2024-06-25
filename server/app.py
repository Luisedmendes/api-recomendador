from flask import Flask, json
from recommender.components.recommender import Recommender

db_file = "./db.sqlite3"

app = Flask(__name__)

@app.route("/recommend/<id_user>", methods=['GET'])  # Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def recommend(id_user):
    r = Recommender(db_file)
    rec = r.get_recommendation(id_user)
    # Retorna um array vazio caso não existam recomendações para este usuário
    return [] if not rec else json.loads(rec)


@app.route("/similar/<id_movie>", methods=['GET'])  # Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def similar(id_movie):
    print(typeof(id_movie))
    r = Recommender(db_file)
    # Obtém a lista de filmes do banco de dados
    movie_list = r.get_movie_list()
    

    # Chama o método get_similar com os parâmetros necessários
    sim = r.get_similar(id_movie, movie_list)
    
    # Retorna um array vazio caso não existam recomendações para este filme
    return sim 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
