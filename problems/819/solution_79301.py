def filtraMultiplos(lista,n):
    """Retorna uma lista contendo todos os elementos da lista original que forem
    divisíveis por n. list, int-> list"""
    i = 0
    multiplos = ()
    while i<len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + lista[i]
        i = i+1
    return lista