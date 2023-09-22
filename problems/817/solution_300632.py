def acima_da_media(lista):
    '''Recebe uma lista com as notas dos alunos e 
    retorna uma lista ordenada com as notas que ficaram 
    acima da média.
    list -> list'''
    acima = []
    media = sum(lista) / len(lista)
    notas = tuple(lista)
    if notas > media:
        acima += [notas]
        return acima