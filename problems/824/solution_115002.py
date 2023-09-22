def uppCons (frase):
    lista = frase.split()
    lista1 = []
    i = 0
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyz' : 
            lista1 = [del lista[i]]
			lista1 = [list.isert(lista,i,'opa')]
        i = i + 1
    return ' '.join(lista1)