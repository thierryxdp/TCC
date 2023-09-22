def acima_da_media(lista):
    '''Função que dadas uma lista com as notas dos alunos e uma média 
    retorna uma lista ordenada com as notas que estiverem acima da média
    list -> list'''
    media = sum(lista)/len(lista)
    list.sort(lista)
    return lista[(list.index(lista, media)) + 1:]