import math
def carros (a,b=5):
	'''
	calcula e retorna o número exato de carros necessarios
	para uma viagem a partir das entradas a, para pessoas, e b, 
    para capacidade do veiculo 
	int, int -> int
	'''
	return (math.ceil(a/b))