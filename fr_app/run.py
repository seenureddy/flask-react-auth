from flask import Flask
from flask_mongoengine import MongoEngine

# local imports
from fr_app.app import api_bp
from fr_app.config import Config

db = MongoEngine()



app = Flask(__name__)
app.register_blueprint(api_bp)

# DB Configuration
app.config.from_object(Config)
# DB Connection
db.init_app(app)
app.run(host='0.0.0.0', debug=True, port=5000)
