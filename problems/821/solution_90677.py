import math
def fatorial(num):
	
    '''
    	Função que dado um número, calcula o fatorial deste número.
        lista:list.
        i:int.
        num:int.
    '''
    lista = [num]
    i=1
    while i < num:
        lista.append(i)
        i += 1
    return prod(sorted(lista))