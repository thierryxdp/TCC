def filtraMultiplos(lista,numero):
    """Filtra os múltiplos de um número contido em uma lista e adiciona estes números em uma nova lista.
    list,int -> list """
    i = 0
    novalista = []
    while i <len(lista):
        if lista[i]%numero == 0:
            novalista.append(lista[i])
        i += 1
        
    return novalista