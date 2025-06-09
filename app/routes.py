from flask import Blueprint, request, jsonify, current_app

bp = Blueprint('routes', __name__)

@bp.route("/cache/<key>", methods=["GET", "POST"])
def cache(key):
    r = current_app.redis
    if request.method == "POST":
        data = request.get_json()
        r.set(key, data["value"])
        return jsonify({"status": "ok"}), 201
    else:
        value = r.get(key)
        return jsonify({"value": value.decode() if value else None})

@bp.route("/publish/<channel>", methods=["POST"])
def publish(channel):
    msg = request.get_json().get("message", "")
    current_app.redis.publish(channel, msg)
    return jsonify({"published": msg})
