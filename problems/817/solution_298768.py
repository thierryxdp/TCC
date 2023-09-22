def acima_da_media (lista, n):
    '''funcao que retorne uma lista ordenada com as notas acima da media'''
    for i in lista:
        if i> n:
            lista.append(n)
            list.sort(lista)
    return [i for i in lista if i> n]