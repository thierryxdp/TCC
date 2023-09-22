def filtraMultiplos(numeros,divisor):
	"""Função que recebe como primeiro argumento uma lista de numeros inteiros e
    retorna uma outra lista que contém somente os números divisíveis pelo número
    inserido como segundo argumento"""
    divisiveis=[]
    indice=0
    while indice<len(numeros):
        if numeros[indice]%divisor==0:
            list.append(divisiveis,numeros[indice])
        indice=indice+1
    return divisiveis