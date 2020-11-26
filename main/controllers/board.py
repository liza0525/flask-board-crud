from flask import request, jsonify
from main import app, db
from main.models.board import Board


# reference : https://woolbro.tistory.com/91

@app.route('/')
def hello():
  return 'Hi!'

@app.route('/board/<board_id>', methods=["GET"])
def get_board(board_id):
  board = Board.query.filter_by(board_id=board_id).all()[0]
  data = {
    'board_id': board.board_id,
    'username': board.username,
    'title': board.title,
    'content': board.content,
  }
  return jsonify(data)

@app.route('/board', methods=["GET"])
def get_board_all():
  boards = Board.query.all()
  board_list = []
  for board in boards:
    data = {
      'board_id': board.board_id,
      'username': board.username,
      'title': board.title,
      'content': board.content,
    }
    board_list.append(data)
  return jsonify(board_list)

@app.route('/board', methods=["POST"])
def add_board():
  username = request.form.get('username')
  title = request.form.get('title')
  content = request.form.get('content')

  board = Board()
  board.username = username
  board.title = title
  board.content = content

  db.session.add(board)
  db.session.commit()

  return '글 저장 완료'