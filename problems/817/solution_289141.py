def acima_da_media(lista):
    '''dada uma lista com notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    a = sum(lista)
    b = len(lista)
    media = a//b
    c = media
    list.sort(lista)
    d = list.index(lista, media)
    return d