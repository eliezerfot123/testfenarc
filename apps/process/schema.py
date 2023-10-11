from marshmallow import Schema, fields


class ProcessSchema(Schema):
    id = fields.Int()
    idBulk = fields.Int()
    retries = fields.Int()
    status = fields.Int()
    name = fields.Str()
