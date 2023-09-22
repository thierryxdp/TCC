def acima_da_media(notas):
    """ Blabla"""
    n = (int(sum(notas))/int(len(notas)) - 0.01)
    list.append(notas,n)
    list.sort(notas)
    return notas[list.index(notas,n)+ 1:]