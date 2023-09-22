def uppCons(lista):
    i=0
    lista=lista[0].upper()
    while i<len(lista):
        if lista[0][i] in 'AEIOUÃÉÍÓÚÊ':
            lista=lista[0].replace(lista[0][i],lista[0][i].lower())
            i+=1
        else:
            i+=1
    return lista