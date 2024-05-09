# from utils.db import db
# from dataclasses import dataclass
# from flask import Flask
# from flask_marshmallow import Marshmallow

# app = Flask(__name__)
# ma = Marshmallow(app)
                 
# @dataclass
# class Tipo_predio(db.Model):
#     id_tipo_predio: int
#     nomre_predio: str

#     id_tipo_predio=db.Column(db.Integer, primary_key=True)
#     nomre_predio=db.Column(db.String(255))

#     def __init__(self, id_tipo_predio, nomre_predio):
#         self.id_tipo_predio = id_tipo_predio
#         self.nomre_predio=nomre_predio

from utils.db import db
class TipoPredio(db.Model):
    __tablename__ = 'tipo_predio'
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nomre_predio = db.Column(db.String(255))

    def __init__(self, id_tipo_predio, nomre_predio):
        self.id_tipo_predio = id_tipo_predio
        self.nomre_predio = nomre_predio