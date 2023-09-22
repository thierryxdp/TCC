import math
def carros(Qp,Cv=5):
    '''Retorna a quantidade de carros necessários, tendo como entra
a quantidade de pessoas Qp, e a capacidade do veículo Cv;
OBS: Seguindo as regras da rodovia um veículo pode transportar até 5
pessoas, podendo variar a sua capacidade;
int,int->int'''
    return math.ceil(Qp/Cv)