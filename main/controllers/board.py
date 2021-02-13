from flask_apispec import marshal_with, use_kwargs, doc
from main import db
from main.controllers import board_bp
from main.models.board import Board
from main.models.resources import (
    BoardSchema, 
    BoardList, 
    RequestBoardCreate
)
from main.controllers import API_CATEGORY

@marshal_with(BoardList, code=200)
@board_bp.route('/', methods=['GET'])
@doc(tag=[API_CATEGORY],
     summary='All boards',
     description='Get all boards')
def get_board_all():
    boards = db.session.query(Board).all()
    board_list = []
    for board in boards:
        data = {
            'board_id': board.board_id,
            'username': board.username,
            'title': board.title,
            'content': board.content,
        }
        board_list.append(data)
    
    return {
        'board_list': board_list
    }


@marshal_with(BoardSchema, code=200)
@board_bp.route('/<board_id>', methods=['GET'])
@doc(tag=[API_CATEGORY],
     summary='One board',
     description='Get one board')
def get_board(board_id):
    board = db.session.query(Board).filter(Board.board_id == board_id).first()
    data = {
        'board_id': board.board_id,
        'username': board.username,
        'title': board.title,
        'content': board.content,
    }
    return data


@use_kwargs(RequestBoardCreate)
@board_bp.route('/', methods=['POST'])
@doc(tag=[API_CATEGORY],
     summary='Create a board',
     description='Create a board with values')
def add_board(username, title, content):
    board = Board()
    board.username = username
    board.title = title
    board.content = content

    db.session.add(board)
    db.session.commit()

    return '글 저장 완료'