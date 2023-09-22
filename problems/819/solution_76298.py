def filtraMultiplos(lista,numero):
    """Dada uma lista de números e um número 'n'
    retorna outra lista dos multiplos desse mesmo número 'n'."""
    indice = 0
    list.sort(lista)
    listaMultiplos = []
    while lista[indice] % numero == 0:
        indice += 1
        listaMultiplos.append(lista[indice])
        return listaMultiplos