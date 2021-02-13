from flask import Blueprint
from main import db

API_CATEGORY = "Board"

board_bp = Blueprint('board', __name__, url_prefix='/api/board/')

from main.controllers import board