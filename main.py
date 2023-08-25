from flask import Flask
app = Flask(__name__)

#lista
lista_animes = ['Anime0', 'Anime1', 'Anime2', 'Anime3', 'Anime4']


#first route
@app.route('/anime')
def anime():
    return "anime"

#second route
@app.route('/anime/<id>')
def animeHorimiyapiece(id):
    return lista_animes[id]





if __name__  == '__main__':
    app.run()
