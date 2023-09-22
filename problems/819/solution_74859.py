def filtraMultiplos(lista, num):
    """Função que retorna uma nova lista contendo todos os elementos da lista
    original que forem divisíveis por num, ou seja, os múltiplos de num.
    list, int -> list"""
    
    nova_lista = []
    i = 0
    
    while i < len(lista):
        if (lista[i] % num) == 0:
            list.append(nova_lista,lista[i])
        i = i+1
    return nova_lista