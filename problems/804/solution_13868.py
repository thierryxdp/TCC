def filtra_pares(numeros):
    	""" Recebe quatro números e filtra os números que são pares os excluindo da Tupla e adicionando os pares em uma nova tupla.
    	int->tupla"""
    numeros = []
    pares = ()

    if numeros % 2 == 0:
    	pares += (numeros)
    return pares