def acima_da_media(notas):
    import math
    a=notas
    media= sum(a)/len(a)
    b= math.floor(media)
    lista2=list.append(a, b)
    a.sort()
    return notas