from utils.db import db
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    idubigeo = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(255))

    def __init__(self, idubigeo, departamento):
        self.idubigeo = idubigeo
        self.departamento = departamento
