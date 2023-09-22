import math

def carros(x,y=5):
    """função que calcula e retorna o numero exato de carros necessários para realizar
    viagem, onde o x é o numero de pessoas, e por padrão os carros possuem 
    capacidade(y) de 5 pessoas, porém existem carros de outras capacidades"""
    return math.ceil(x/y)