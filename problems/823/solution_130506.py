def faltante(lista_de_pecas):
    
    lista_de_pecas.sort()
    i = 1
    while lista_de_pecas[i] - lista_de_pecas[i-1] == 1:
        i += 1
    
    return lista_de_pecas[i] + 1