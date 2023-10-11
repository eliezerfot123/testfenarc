from config.settings import db
from apps.process.models import Process
from apps.process.schema import ProcessSchema as Schema

class ProcessServices():
    def __init__(self):
        self.db = db
        self.process = Process

    def get_process(self, status: int):
        result = self.process.query.filter(Process.status==status).all()
        return result
    
    def add_process(self, process: Schema):
        result = self.process(**process)
        db.session.add(result)
        db.session.commit()
        return result