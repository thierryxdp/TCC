import math

def carros(p,c=5):
 """funcao que calcula a quantidade carros necessarios dado o numero de pessoaas p e a capacidade c de um carro, sendo a capacidade convencional igual a 5 pessoas"""
 return math.ceil(p/c)