from flask import Flask
from utils.db import db
from services.predio_routes import predio_routes
#from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://modulo4:modulo4@137.184.120.127:5432/sigcon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)

# Inicializar la extensión SQLAlchemy con la aplicación Flask
db.init_app(app)

# Registrar las rutas del blueprint
app.register_blueprint(predio_routes)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
