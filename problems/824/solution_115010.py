def uppCons (frase):
    lista = frase.split()
    i = 0
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyz' : 
            del lista[i]
            lista = lista
        i = i + 1
        lista = lista
    return ' '.join(lista)