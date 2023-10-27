import argparse

from flask import Flask
from flask_restful import Api

from apps.memory.routes import MemoryView, SingleMemoryView


app = Flask(__name__)

app.config.from_object("settings.config.EnvConfig")

api_router = Api(app, prefix="/api/v1")
api_router.add_resource(MemoryView, "/memories")
api_router.add_resource(SingleMemoryView, "/memories/<string:memory_alarm_id>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1", help="Host IP address")
    parser.add_argument("--port", type=int, default=5000, help="Port number")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=app.config["DEBUG"])
