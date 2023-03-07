from flask import Flask, jsonify
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route("/")
def root():
    """The root route"""
    return jsonify({"status": "ok"})
