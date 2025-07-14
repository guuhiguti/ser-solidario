from flask import Blueprint, render_template

jc_route = Blueprint('jc', __name__)

@jc_route.route('/jovem-conectado')
def jovem_conectado():
    return render_template('jovem-conectado.html')