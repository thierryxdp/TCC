def filtraMultiplos(lista, numero) -> list:
    """ recebe uma lista de números como entrada, e retorna
    outra lista contendo todos os elementos da lista original que
    forem divisíveis por n """
    lista1 = list(lista)
	total = ()
    i = 0
    
    while i < len(lista1):
        if lista1[i]%numero == 0:
            total = total + lista1[i]
        i = i + 1
    return total