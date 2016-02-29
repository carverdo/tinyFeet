"""
Simple form-filler..
"""
__author__ = 'donal'
__project__ = 'tinyFeet'

from flask import Flask

def create_app():
    app = Flask(__name__)
    from .project import proj
    app.register_blueprint(proj)
    return app