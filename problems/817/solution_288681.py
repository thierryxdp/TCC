def acima_da_media(lista):
    '''dada uma lista com as notas de uma turma, retorna uma lista com as notas maiores que a media
    list -> list'''
    total = 0
    final = []
    for i in lista:
        total += i
    media = total / len(lista)
    for i in lista:
        if i > media:
            list.append(final, i)
    list.sort(final)
    return final