"""
Simple form-filler.
"""
__author__ = 'donal'
__project__ = 'tinyFeet'

from config import build_mc_config
mc = build_mc_config()

from flask import Flask

def create_app():
    app = Flask(__name__)
    from .project import proj
    app.register_blueprint(proj)
    return app
