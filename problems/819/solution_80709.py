def filtraMultiplos(lista,n):
    """função que dada uma lista de inteiros retorna outra lista;lista-->lista"""
    lista2 = []
    prox = 0
    while prox <len(lista):
        if lista[prox]%n == 0:
            lista2 = lista2 + [lista[prox]]
        prox = prox + 1
    return lista2