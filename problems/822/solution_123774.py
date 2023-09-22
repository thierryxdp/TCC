def repetidos(lista):
    '''Verifica se o numero na posição y é igual ao numero na posição y-1
    list->int'''
    cont = 0
    for y in range(len(lista)):
        if lista[y] == lista[y-1]:
            cont += 1
    return cont