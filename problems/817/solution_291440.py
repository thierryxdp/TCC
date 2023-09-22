def acima_da_media(lista):
    '''Função que dadas uma lista com as notas dos alunos e uma média 
    retorna uma lista ordenada com as notas que estiverem acima da média
    list -> list'''
    media = sum(lista)/len(lista)
    list.insert(lista, 0, media)
    list.sort(lista)
    if list.count(lista, media) < 2:
        return lista[(list.index(lista, media)) + 1:]
    else:
        return lista[(list.index(lista, media)) + list.count(lista, media):]