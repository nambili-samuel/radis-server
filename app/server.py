from flask import Flask
from redis import Redis
from app.routes import bp

def create_app():
    app = Flask(__name__)
    redis_url = app.config.get("REDIS_URL", "redis://localhost:6379/0")
    app.redis = Redis.from_url(redis_url)
    app.register_blueprint(bp)
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
