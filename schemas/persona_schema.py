from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    id_persona = fields.Integer()
    nombres = fields.String()
    fecha_nacimiento = fields.String()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)