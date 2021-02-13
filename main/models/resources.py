from marshmallow import Schema, fields, validate


class BoardSchema(Schema):
    board_id = fields.Int()
    username = fields.Str()
    title = fields.Str()
    content = fields.Str()


class BoardList(Schema):
    board_list = fields.List(fields.Nested(BoardSchema))


class RequestBoardCreate(Schema):
    username = fields.Str()
    title = fields.Str()
    content = fields.Str()