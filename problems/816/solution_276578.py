def maiores(lista,n):
    """A função recebe uma lista numérica e um inteiro como entrada e retorna uma lista com os números maiores que o inteiro de entrada;
    list,n->list"""
    Nova_lista=lista[:]
    list.extend(Nova_lista,[n])
    list.sort(Nova_lista)
    del Nova_lista[:list.index(Nova_lista,n)+1]
    return Nova_lista