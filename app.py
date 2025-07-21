from flask import Flask, render_template, url_for

app = Flask(__name__)

""" Rotas 

Página Inicial - "/"
Formulário de Ajuda - "/form-ajuda"
Formulário de Colaboração - "/form-colab"

Sobre o Projeto - "/sobre"



"""

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/preciso-ajuda")
def ajuda():
    return render_template('form-ajuda.html')

@app.route("/quero-colaborar")
def colab():
    return render_template('form-colab.html')




app.run(debug=True)