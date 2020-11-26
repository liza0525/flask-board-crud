from main import db
from flask_sqlalchemy import SQLAlchemy

class Board(db.Model):
  __tablename__ = 'board'
  board_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  title = db.Column(db.String(50))
  username = db.Column(db.String(15))
  content = db.Column(db.String(200))