def filtraMultiplos(lista, n):
    '''filtra os multilps de n na lista
    lista, int -> lista'''
    indice = 0
    novaLista = []
    while indice <= len(lista):
        if indice%n == 0:
            novaLista = novaLista + [lista[indice]]
        i = i + 1
    return novaLista