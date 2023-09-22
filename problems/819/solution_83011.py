def filtraMultiplos(lista,n):
    """Funcao que dada uma lista e um numero retorna todos os
    elementos multiplos desse numero"""
    multiplos = []
    numeros = 0
    while numeros < len(lista):
        if lista[numeros] % n = 0:
            multiplos = multiplos + lista[numeros]
        numeros = numeros + 1
    return multiplos