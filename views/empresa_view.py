from flask_restful import Resource
from application.controllers import empresa_controller
from application.schemas import empresa_schema
from application.entities import empresa_entity
from flask import make_response,request
from marshmallow import ValidationError,pre_load

class Empresa(Resource):
    def get(self,id):
        return empresa_controller.listar_empresa(empresa_id=id)
        #result = empresa_schema.dump(empresas)
        #return {"empresas":result}

    def delete(self,id):
        return empresa_controller.excluir_empresa(empresa_id=id)
    
class EmpresaList(Resource):

    def post(self):
        #request.get_json()
        data = request.json

        entidade = empresa_entity.Empresa(
            empresa_id=data["empresa_id"],
            codigo_filial=data["codigo_filial"],
            nome=data["nome"],
            cnpj=data["cnpj"],
            grupo=data["grupo"],
            regime_fiscal=data["regime_fiscal"],
            atividades=data["atividades"],
            uf=data["uf"],
            ie=data["ie"],
            plataforma=data["plataforma"],
            data_de_entrada=data["data_de_entrada"],
            abertura_na_empresa=data["abertura_na_empresa"],
            porte = data["porte"]
        )
        empresa = empresa_controller.criar_empresa(entidade)

        return make_response(empresa)
    
    def get(self):
        return make_response(empresa_controller.listar_empresas())