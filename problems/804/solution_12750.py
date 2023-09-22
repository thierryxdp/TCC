def filtra_pares(x,y,z,w):
    '''Função que recebe uma tupla com quatro elementos inteiros e retorne uma nova tupla contendo apenas os elementos pares da tupla original
    tupla, tupla, tupla, tupla -> tupla'''
    lista1 = [x,y,z,w]
    lista2 = []
    for i in lista1:
        if i % 2 == 0:
            lista2.append(i)
    return lista2