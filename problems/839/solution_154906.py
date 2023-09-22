#importar o math primeiro
from math import*

#questão 2 quantos carros
def carros(p,c=5):
    '''Para calcular a quantidade de veículos é necessario resolver a conta
    ("p" são as pessoas que vão a viagem(tem que ser número inteiro,
    pois não existe metade de uma pessoa)),("c" é a capacidade máxima de pessoas
    em um carro(tem que ser número inteiro, pois não existe metade de uma pessoa)):
    p/c'''
    return ceil(int(p)/int(c))