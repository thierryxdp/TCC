def filtraMultiplos(lista,numero):
    """Dada uma lista de números e um número 'n'
    retorna outra lista dos multiplos desse mesmo número 'n'."""
    indice = 0
    listaMultiplos = []
    while indice < len(lista):
        if lista[indice] % numero == 0:
            listaMultiplos.append(lista[indice])
        indice += 1
        return listaMultiplos