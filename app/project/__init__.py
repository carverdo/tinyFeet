__author__ = 'donal'
__project__ = 'tinyFeet'

from flask import Blueprint
proj = Blueprint('proj', __name__)
from . import views