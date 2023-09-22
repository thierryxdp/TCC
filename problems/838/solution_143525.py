import math

def num_bombons(d, p):
''' Usando a quantidade de dinheiro 'd', e o preço unitário de um bombom 'p',
Divide o dinheiro que ele tem pelo preço unitário do bombom '''

	return math.floor(d/p)

	#Casos testes:
    #(10, 1.05) => return 9
    #(5, 0.5) => return 10
    #(18, 4) => return 4