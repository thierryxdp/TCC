def acima_da_media(notas):
    '''Esta funcao calcula as notas que ficaram acima da media de uma turma.'''
    '''list --> list'''
    media = (soma_das_notas)/quantidade_de_nota
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    acima_da_media = notas[(indice + 1):]
    return acima_da_media