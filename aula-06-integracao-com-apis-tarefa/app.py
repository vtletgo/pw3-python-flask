from flask import Flask
from controllers.spacex_controller import spacex_bp


def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.register_blueprint(spacex_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
