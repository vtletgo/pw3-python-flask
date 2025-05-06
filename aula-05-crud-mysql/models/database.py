from flask_sqlalchemy import SQLAlchemy


# criar uma instância do sqlalchemy na variável
db = SQLAlchemy()

# criando o model (classe)
class Game(db.Model):
    # criando os atributos da tabela
    id = db.Column(db.Integer(), primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.preco = preco
        self.plataforma = plataforma
        self.quantidade = quantidade
        
    
class Console(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(150))
    fabricante = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    
    # método construtor da classe do python
    def __init__(self, nome, fabricante, ano, preco, quantidade):
        self.nome = nome
        self.fabricante = fabricante
        self.ano = ano
        self.preco = preco
        self.quantidade = quantidade
        
    