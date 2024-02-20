from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()

ma = Marshmallow()


def create_app():
    #Instancia o app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fiscal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'F'

    ma.init_app(app)

    from flask_restful import Api
    api = Api(app)
    from application.views import empresa_view

    api.add_resource(empresa_view.Empresa,"/empresas/<id>")
    api.add_resource(empresa_view.EmpresaList,"/empresas")


    db.init_app(app)
    with app.app_context():
        db.create_all()


    return app


    