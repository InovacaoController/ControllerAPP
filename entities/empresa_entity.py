from typing import Optional
import datetime

class Empresa:
    def __init__(self,empresa_id,nome,cnpj,codigo_filial,grupo,regime_fiscal,atividades,uf,ie,plataforma,data_de_entrada=None,abertura_na_empresa=None,porte=None) -> None:
        self.empresa_id = empresa_id
        self.codigo_filial = codigo_filial
        self.nome = nome
        self.cnpj = cnpj
        self.grupo = grupo
        self.regime_fiscal = regime_fiscal
        self.atividades = atividades
        self.uf = uf
        self.ie = ie
        self.plataforma=plataforma
        self.data_de_entrada = data_de_entrada
        self.abertura_na_empresa = abertura_na_empresa
        self.porte = porte