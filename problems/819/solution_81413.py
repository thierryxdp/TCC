def filtraMultiplos(lista, n):
    """função que recebe uma lista de numeros e um numero n e retorna outra lista com os números da lista original que forem
	divisíveis por n
	list, float -> list"""
    
    i = 0 
    divisiveis = ()
    
    while len(lista) > i:
        if int(lista[i])%n == 0:
            divisiveis = divisiveis + (lista[i],)
        i = i + 1
    return list(divisiveis)