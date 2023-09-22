def filtraMultiplos(lista,n):
    """Funcao que dada uma lista e um numero retorna todos os
    elementos multiplos desse numero"""
    multiplos = []
    numeros = 0
    while numeros < len(lista):
        x = lista[numeros]
        if x % n = 0:
            list.append(multiplos,x)
        numeros = numeros + 1
    return multiplos