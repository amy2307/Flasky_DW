from utils.ma import ma
from model.predio import Predio
from marshmallow import fields
from schemas.tipo_predio_schema import TipoPredioSchema
from schemas.ubigeo_schema import UbigeoSchema
from schemas.persona_schema import PersonaSchema

class PredioSchema(ma.Schema):
    class Meta:
        model  = Predio
        fields = ('id_predio',
                  'id_tipo_predio',
                  'descripcion',
                  'ruc',
                  'telefono',
                  'correo',
                  'direccion',
                  'idubigeo',
                  'id_persona',
                  'url_imagen',
                  'tipo_predio',
                  'persona',
                  'ubigeo')
    
    tipo_predio = ma.Nested(TipoPredioSchema)
    persona = ma.Nested(PersonaSchema)
    ubigeo = ma.Nested(UbigeoSchema)


predio_schema = PredioSchema()
predios_schema = PredioSchema(many=True)