def filtraMultiplos(lista,n):
    """retorna uma lista contendo todos os itens
    da lista de entrada que forem divisiveis
    pelo valor n
    list, int -> list"""
    lista_multiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            lista_multiplos += [lista[i]]
        i += 1
    return lista_multiplos