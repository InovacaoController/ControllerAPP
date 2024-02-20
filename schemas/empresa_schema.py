from application.app import ma
from application.models import empresa_model

class EmpresaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = empresa_model.Empresa
        load_instance = True