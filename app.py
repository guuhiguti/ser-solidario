from flask import Flask
from routes.home import home_route
from routes.jc import jc_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(jc_route)

app.run(debug=True)