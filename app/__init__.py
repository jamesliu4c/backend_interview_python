from flask import Flask, jsonify, request
import requests
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

API_ROOT = "https://winter-dawn-3615.fly.dev"

@app.route("/")
def root():
    """The root route"""
    return jsonify({"status": "ok"})


@app.route("/advertiser/")
def advertiser():
    """Gets the advertiser information from the partner API
    """
    if not request.args.get("id"):
        return jsonify({"error": "Must supply query for id"}), 404
    advertiser_id = request.args["id"]

    resp = requests.get(f"{API_ROOT}/advertiser/{advertiser_id}/")

    if not resp.ok:
        return jsonify({"error": resp.reason}), resp.status_code
    
    advertiser = resp.json()
    return jsonify({"advertiser": advertiser})



@app.route("/campaigns/")
def campaigns():
    """Gives campaigns, a list of flattened objects. Each object is a campaign,
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
    return jsonify({"error": "Not implemented"}), 501