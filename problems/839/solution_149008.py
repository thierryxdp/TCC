import math

def carros(p,q=5):
    '''Função que calcula e retorna quantos carros de capacidade q serão
    necessários para levar p pessoas através da divisão entre p e q;
    p=int,q=int-> int'''
    return math.ceil(p/q)