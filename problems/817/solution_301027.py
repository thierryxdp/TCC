def acima_da_media(notas):
    '''list->list que retorna as notas acima da media'''
    if len(notas)==1:
        list.clear(notas)
        return notas
    else:
        media=(sum(notas)/len(notas))
        list.append(notas,media)
        list.sort(notas)
        pos=list.index(notas,media)
        del notas[0:pos+1]
        return notas