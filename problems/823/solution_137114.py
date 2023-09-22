def faltante(lista_pecas):
    lista_pecas = []
    i=0
    while i < len(lista_pecas):
        if i + 1 != lista_pecas[i]:
            return i + 1
        return len(lista_pecas) + 1