from flask import Blueprint, render_template

acoes_route = Blueprint('acoes', __name__)

@acoes_route.route('/acoes')
def acoes():
    return render_template('acoes.html')