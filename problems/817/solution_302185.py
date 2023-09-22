def acima_da_media(notas):
    '''Código que recebe notas, seleciona as acima da média, e as coloca em ordem crescente
    list -> list'''
    listamedia = list()
    media = sum(notas)/len(notas)
    for soma in notas:
        if soma>media:
            listamedia.append(soma)
    listamedia.sort()
    return listamedia