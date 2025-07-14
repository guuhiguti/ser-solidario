from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def index():
    return render_template('index.html')

@home_route.route('/preciso-ajuda')
def preciso_ajuda():
    return render_template('form-ajuda.html')

@home_route.route('/quero-colaborar')
def quero_colaborar():
    return render_template('form-colab.html')


