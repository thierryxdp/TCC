def uppCons(frase):
    i=0
    FRaSe = ''
    lista = list(frase)
    while i<len(frase):
        if lista[i] in 'bcdfghjklmnpqrstvwzç':
            lista[i] = str.upper(lista[i])
        i=i+1
    FRaSe= ''.join(lista)
    return FRaSe