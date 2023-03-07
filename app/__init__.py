from flask import Flask, jsonify, request
import requests
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route("/")
def root():
    """The root route"""
    return jsonify({"status": "ok"})


@app.route("/campaign/")
def campaign():
    """Gives campaigns, a flattened list of objects. Each object is a campaign,
    which should have all of the entries from the partner campaign endpoint and
    the partner campaign stats endpoint.
    
    Like:

    >>> campaign("2023-01-01", "2023-01-31")
    {
        "campaigns": [
            {
                "id": 0, type: "", "name": "", "date_start": "", ...
                "impressions": 0, "spend": 0, "unique_users": 0, ...
            },
            ...
        ]
    }
    """
    print(request.args)

    return jsonify({"error": "Not implemented"}), 500