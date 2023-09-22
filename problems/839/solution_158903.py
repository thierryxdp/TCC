def carros(pessoas,numero=5):
    '''Função que baseado no número de pessoas e no número de pessoas que os carros comportam diz quantos carros serão utilizados'''
	import math
    return math.ceil(pessoas/numero)