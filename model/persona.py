from utils.db import db
class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.String(255))


    def __init__(self, id_persona, nombres, fecha_nacimiento):
        self.id_persona = id_persona
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento