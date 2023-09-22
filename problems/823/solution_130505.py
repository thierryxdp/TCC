def faltante(lista_de_pecas):
    
    lista_de_pecas.sort()
    i = 0
    while lista_de_pecas[i+1] - lista_de_pecas[i] == 1:
        i += 1
    
    return lista_de_pecas[i] + 2