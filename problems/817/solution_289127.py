def acima_da_media(lista):
    '''dada uma lista com notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    a = sum(lista)
    b = len(lista)
    media = a/b
    if media not in lista:
        lista = lista + [media]
        list.sort(lista)
        x = list.index(lista, media)
        return lista[x+1:]
    else:
        list.sort(lista)
        return lista[media:]