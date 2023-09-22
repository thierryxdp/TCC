def filtraMultiplos(lista, n):
    """Função que dada uma lista e um número inteiro n retorna uma lista_n contend apenas os múltiplos de n.
    list, int --> list"""
    i = 0
    lista_n = []
    while (i < len(lista)):
        if (lista[i] % n == 0):
            list.append(lista_n, lista[i])
            
        i += 1
        
    return lista_n