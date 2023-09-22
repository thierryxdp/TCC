def acima_da_media(notas):
    '''retorna uma lista ordenada com as notas que ficaram acima da média; list-->list.'''
    m=sum(notas)/len(notas)
    list.append(notas,m)
    list.sort(notas)
    x=list.index(notas,m)
    if len(notas)==2:
        return []
    else:
        return notas[x+1:]