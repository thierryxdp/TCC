def filtraMultiplos(lista, numero) -> list:
    """ recebe uma lista de números como entrada, e retorna
    outra lista contendo todos os elementos da lista original que
    forem divisíveis por n """
    
	total = []
    i = 0
    
    while i < len(lista):
        if lista[i]%numero == 0:
            total = total + lista[i]
        i = i + 1
        
    return lista