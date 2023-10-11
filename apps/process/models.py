from config.settings import db


class Process(db.Model):
    __tablename__ = 'ElementsToProcess'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idBulk = db.Column(db.Integer, nullable=False)
    retries = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, idBulk, retries, status, name):
        self.idBulk = idBulk
        self.retries = retries
        self.status = status
        self.name = name
