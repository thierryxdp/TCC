def uppCons (frase):
    lista = frase.split()
    i = 0
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyz' : 
            del lista[i]
			list.isert(lista,i,)
        i = i + 1
    return ' '.join(lista)