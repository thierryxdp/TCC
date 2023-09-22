def acima_da_media(notas):
    '''list->list que retorna as notas acima da media'''
    media=(sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    pos=list.index(notas,media)
    del notas[:pos+1]
    return notas