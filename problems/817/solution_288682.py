def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista com as notas maiores que a media
    list -> list'''
    total = sum(lista)
    final = []
    media = total / len(lista)
    for i in lista:
        if i > media:
            list.append(final, i)
    list.sort(final)
    return final