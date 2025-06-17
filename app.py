from flask import Flask
from extensions import db
from flask_cors import CORS
from blueprints.landing_page_routes import landing_page_register_blueprints
from blueprints.machine_learning_routes import machine_learning_blueprints
from blueprints.python_routes import python_blueprints
from blueprints.deep_learning_routes import deep_learning_blueprints

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
landing_page_register_blueprints(app)
machine_learning_blueprints(app)
python_blueprints(app)
deep_learning_blueprints(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    

