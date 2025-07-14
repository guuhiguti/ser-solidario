from flask import Blueprint, render_template, url_for

jc_route = Blueprint('jovem-conectado', __name__)

@jc_route.route('/jovem-conectado')
def jc():
    return render_template('jovem-conectado.html')
