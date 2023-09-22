def filtraMultiplos(lista, n):
    '''função que verifica se o numero dado é múltiplo de n; list, int -> list'''
    segundaLista = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            segundaLista.append(lista[i])
        i = i + 1
    return segundaLista