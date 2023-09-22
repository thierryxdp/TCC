def acima_da_media(lista, media):
    '''Função que dadas uma lista com as notas dos alunos e uma média 
    retorna uma lista ordenada com as notas que estiverem acima da média
    list, float -> list'''
    list.insert(lista, media)
    list.sort(lista)
    return lista[(list.index(lista, media)) + 1:]