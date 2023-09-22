def acima_da_media (nota):
    '''retorna uma lista ordenada com as notas acima da media'''
    '''list -> list'''
    soma=sum(nota)
    n=len(nota)
    media=(soma//n)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i = list.index(nota,media)
    lista = nota [0:i]
    list.sort(lista)
    return lista