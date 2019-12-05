import os,datatime
from peewee import *

arq = 'automobilismo.db'

db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pista(BaseModel):
    nome_pista = CharField()
    tamanho = CharField()
    pais = CharField()
    numero_curvas = IntegerField()
     def __str__(self):
        return self.nome_pista+", "self.tamanho+", "self.pais+", "+str(self.numero_curvas)

class Equipe(BaseModel):
    nome_equipe = CharField()
    fundacao = CharField()
    pais_origem = CharField()
    categoria = ForeingKeyField()
    chef_equipe = ForeingKeyField()
    motor = ForeingKeyField()
    carro = ForeingFeyField()
    piloto_1 = ForeingFeyField()
    piloto_2 = ForeingFeyField()
    def __str__(self):
        return self.nome_equipe+", "self.fundacao+", "self.pais_origem+", "self.categoria+", "self.chef_equipe+", "self.motor+", "self.carro+", "self.piloto_1+", "self.piloto_2 

class Categoria(BaseModel):
    nome_categoria = CharField()
    potencia = CharField()
    def __str__(self):
        return self.nome_categoria+", "self.potencia

class Piloto(BaseModel):
    nome_piloto = CharField()
    idade = integerfield()
    equipe = ForeingKeyField()
    carreira = charfiel()
    penalidades = ForeingKeyField()
    pista = ForeingKeyField()
    def __str__(self):
        return self.nome_piloto+", "+str(self.idade)+", "self.equipe+", "self.carreira+", "self.penalidades+", "self.pista

class Carro(BaseModel):
    cor = CharField()
    equipe = ForeingKeyField()
    pneu = CharField()
    def __str__(self):
        return self.cor+", "self.equipe+", "self.pneu

class Chef_de_Equipe(BaseModel):
    nome_chef = CharField()
    idade = IntegerField()
    carreira = CharField()
    def __str__(self):
        return self.nome_chef+", "+str(self.idade)+", "self.carreira

class Camp_Pilotos(BaseModel):
    piloto = ForeingFeyField()
    pontuacao = IntegerField()
    equipe = ForeingFeyField()
    def __str__(self):
        return self.piloto+", "+str(self.pontuacao)+", "self.equipe

class Camp_Construtores(BaseModel):
    pontuacao = IntegerField()
    equipe = ForeingKeyField()
    piloto_1 = ForeingKeyField()
    piloto_2 = ForeingKeyField()
    def __str__(self):
        return +str(self.pontuacao)+", "self.equipe+", "self.piloto_1+", "self.piloto_2

class Forenecedor_Motor(BaseModel):
    nome_motor = CharField()
    potencia = CharField()
    montador = CharField()
    def __str__(self):
        return self.nome_motor+", "self.potencia+", "self.montador

class Penalizacao(BaseModel):
    nome_penalidade = CharField()
    motivo = CharField()
    tempo = CharField()
    avisos = CharField()
    bandeira = CharField()
    def __str__(self):
        return self.nome_penalidade+", "self.motivo+", "self.tempo+", "self.avisos+", "self.bandeira

if __name__=="main":

    if os.path.exists(arq)
        os.remove(arq)

    db.connect()
    db.create_tables([Pista, Equipe, Categoria, Piloto, Carro, Chef_de_Equipe, Camp_Pilotos, Camp_Construtores, Forenecedor_Motor, Penalizacao])

pista1 = Pista.create(nome_pista="Melborne", tamanho="5,303 km", pais="Australia", numero_curvas=16)
categoria1 = Categoria.create(nome_categoria="Formula 1", potencia = "927 cv")
penalidade = Penalizacao.create(nome_penalidade = 'corte de curva', motivo = "cortou a curva 10", tempo = "3 segundos", avisos = "nenhum aviso", bandera = "preta e branca")
penalidade2 = Penalizacao.create(nome_penalidade = "ultrapassagem ilegal", motivo = "ultrapassou em zona invalida", tempo = "0 segundos, devolver a posição", avisos = "nenhum aviso", bandeira = "amarela")
piloto1 = Piloto.create(nome_piloto ="Sebastian Vettel", idade = 32, equipe = equipe1, carreira = "tetra campeao pela RBR", penalidade = penalidade, pista = pista1)
piloto2 = Piloto.create(nome_piloto ="Charles Leclerc", idade = 20, equipe = equipe1, carreira = "estrou na f1 pela alfa romeu", penalidade = penalidade2, pista = pista1)
carro1 = Carro.create(cor = "vermelho e preto", equipe = equipe1, pneu = "Pirreli")
chefdeequipe1 = Chef_de_Equipe.create(nome_chef ="Mattia Binotto", idade = 50, carreira = "formado em engenharia assumio a equipe em 2019")
motor1 = Forenecedor_Motor.create(nome_motor = "Ferrari 064", potencia = "927 cv", montador = "Ferrari")
equipe1 = Equipe.create(nome_equipe="Scuderia Ferrari", fundacao = 1939, pais_origem = "Italia", categoria = categoria1, chef_equipe = chefdeequiepe1, motor = motor1, carro = carro1, piloto_1 = piloto1, piloto_2 = piloto2)
camppilotos1 = Camp_Pilotos.create(piloto = piloto1, pontuacao = 247, equipe = equipe1)
campcontrutores1 = Camp_Construtores.create(pontuacao = 504, equipe = equipe1, piloto_1= piloto2, piloto_2 = piloto2)

print (equipe)
print (campcontrutores1)
print (camppilotos1)
