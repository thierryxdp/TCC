import math
def carros(p , v=5):
	'''Esta função calcula a quantidade de veiculos necessários para realizar a viagem de X números de pessoas), assumimos por padrão uma quantidade máxima de 5 pessoas por carro'''
    resultado = math.ceil (p/v)
    return resultado