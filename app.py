from flask import Flask
from routes.home import home_route
from routes.sobre import sobre_route
from routes.acoes import acoes_route
from routes.jc import jc_route
from routes.contato import contato_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(sobre_route)
app.register_blueprint(acoes_route)
app.register_blueprint(jc_route)
app.register_blueprint(contato_route)


app.run(debug=True)