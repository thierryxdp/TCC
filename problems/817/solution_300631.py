def acima_da_media(lista):
    '''Recebe uma lista com as notas dos alunos e 
    retorna uma lista ordenada com as notas que ficaram 
    acima da média.
    list -> list'''
    media = sum(lista) / len(lista)
    return media