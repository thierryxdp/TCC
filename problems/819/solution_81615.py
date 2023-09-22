def filtraMultiplos(lista,n):
    """dado uma lista de numeros e um numero qualquer, retorna uma 
    outra lista contendo todos os numeros da lista original que 
    forem divisiveis por esse numero qualquer
    list, int --> list"""
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos