from application.models import empresa_model
from application.entities import empresa_entity
from application.app import db  
from flask import jsonify
from openpyxl import Workbook

def criar_empresa(dados:empresa_entity.Empresa):
    
    if empresa_existe(dados.empresa_id):
        nova_empresa = empresa_model.Empresa(
            empresa_id = dados.empresa_id,
            codigo_filial=dados.codigo_filial,
            nome=dados.nome,
            cnpj=dados.cnpj,
            grupo=dados.grupo,
            regime_fiscal=dados.regime_fiscal,
            atividades=dados.atividades,
            uf=dados.uf,
            ie=dados.ie,
            plataforma=dados.plataforma,
            data_de_entrada=dados.data_de_entrada,
            abertura_na_empresa=dados.abertura_na_empresa,
            porte=dados.porte
                )   
        db.session.add(nova_empresa)
        db.session.commit()

        return jsonify({"status":"Created"}),201
    
    print("Empresa não existe")

def empresa_existe(id):

    return True if empresa_model.Empresa.query.filter_by(empresa_id=id).first() is not None else False
def atualizar_empresa(dados:empresa_entity.Empresa):
    #Reescreve todas as informações da empresa, mesmo que altere apenas uma ou duas
    empresa = empresa_model.Empresa.query.filter_by(empresa_id=dados.empresa_id).first()
    if empresa:
        empresa.nome = dados.nome
        empresa.cnpj = dados.cnpj
        empresa.grupo = dados.grupo
        empresa.regime_fiscal = dados.regime_fiscal
        empresa.atividades = dados.atividades
        empresa.uf = dados.uf
        empresa.id = dados.ie
        empresa.plataforma = dados.plataforma
        empresa.porte = dados.porte
        db.session.commit()
        return jsonify({"message":"success"}),200
        
def listar_empresa(empresa_id):
    query = empresa_model.Empresa.query.filter_by(empresa_id=empresa_id).first()
    return jsonify({
        "status":"listed",
        "data":[query.to_json()]
    }),200

def listar_empresas():
    query = empresa_model.Empresa.query.all()

    print(query)

    
    if len(query) > 0:
        return jsonify({
            "data":[empresa.to_json() for empresa in query]
        }),200  

    return jsonify({
        "message":"Sem empresas cadastradas"
    }),200

def excluir_empresa(empresa_id):
    query = empresa_model.Empresa.query.filter_by(empresa_id=empresa_id).first()
    query.ativa = False
    db.session.commit()

    return jsonify({
        "message":"empresa excluida com sucesso"
    }),200

def alterar_grupo_em_lote(novo_grupo,empresas):
    for empresa in empresas:
        query = empresa_model.Empresa.query.filter_by(empresa_id=empresa).first()
        if query is not None:
            query.grupo = novo_grupo

    db.session.commit()
    return jsonify(
        {"message":"sucess"}
    ),200

def alterar_regime_em_lote(novo_regime,empresas):
    for empresa in empresas:
        query = empresa_model.Empresa.query.filter_by(empresa_id=empresa).first()
        if query is not None:
            query.regime = novo_regime

    db.session.commit()
    return jsonify(
        {"message":"sucess"}
    ),200

def gerar_planilha_de_empresas():
    empresas = empresa_model.Empresa.query.all()
    wb = Workbook()
    ws=wb.active

    for index,empresa in enumerate(empresas):
        for coluna,dado in len(empresa):
            ws.cell(index + 1,coluna + 1).value = dado
        

    wb.save("Planilha de Empresas.xlsx")

    return 