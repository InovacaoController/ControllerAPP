from application.app import db  
class Empresa(db.Model):
    empresa_id = db.Column(db.Integer)
    codigo_filial = db.Column(db.Integer,default=1)
    nome = db.Column(db.String(100),nullable=False)
    cnpj = db.Column(db.String(14),primary_key=True)
    grupo = db.Column(db.String(14))
    regime_fiscal = db.Column(db.String(2))
    atividades = db.Column(db.String(14))
    uf = db.Column(db.String(2))
    ie = db.Column(db.String(15))
    plataforma = db.Column(db.String(20))
    ativa=db.Column(db.Boolean,default=True)
    porte = db.Column(db.String(5))

    data_de_entrada = db.Column(db.Date)
    abertura_na_empresa = db.Column(db.Boolean,default=False)
    
    def to_json(self):
        return {
            'empresa_id': self.empresa_id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'grupo': self.grupo,
            'regime_fiscal': self.regime_fiscal,
            'atividades': self.atividades,
            'uf': self.uf,
            'ie': self.ie,
            'plataforma': self.plataforma,
            'ativa': self.ativa,
            'data_de_entrada': self.data_de_entrada.strftime('%Y-%m-%d') if self.data_de_entrada else None,  # Formata a data como string
            'abertura_na_empresa': self.abertura_na_empresa
        }
    
class SCP(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cnpj_empresa = db.Column(db.String(14),db.ForeignKey)
    nome = db.Column(db.String(100),nullable=False)
