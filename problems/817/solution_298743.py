def acima_da_media (lista, n=5):
    '''funcao que retorne ordenado as notas acima da media'''
    for i in lista:
        if i > n:
            lista.append(lista)
            list.sort(lista)
        return [i for i in lista if i> n]