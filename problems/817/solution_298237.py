def acima_da_media(notas):
    '''retorna uma lista com as notas acima da media'''
    soma=sum(notas)
    Ni=len(notas)
    media=(soma//Ni)
    list.append(notas,media)
    list.sort(notas)
    list.reverse(notas)
    i=list.index(notas,media)
    lista=notas[0:i]
    list.sort(lista)
    return lista