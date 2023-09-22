def faltante(lista_de_pecas):
    
    lista_de_pecas.sort()
    i = 0
    while i < len(lista_de_pecas) and lista_de_pecas[i] == i + 1:
        i += 1
    
    return i + 1