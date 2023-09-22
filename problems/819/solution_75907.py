def filtraMultiplos(lista, numero):
    """Função que recebe uma lista de numeros e um numero. Retorna todos os numeros da lista divisiveis por n
    list, int --> list"""
    numeros=[]
    a= 0
    while a <len(lista):
        if lista [a]%numero == 0:
            numeros= numeros + [lista[a],]
        a= a+1
    return numeros