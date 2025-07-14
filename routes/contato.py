from flask import Blueprint, render_template

contato_route = Blueprint('contato', __name__)

@contato_route.route('/contato')
def contato():
    return render_template('contato.html')