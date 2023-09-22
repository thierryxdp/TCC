def uppCons (frase):
    lista = frase.split()
    i = 0
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyz' :
            palavra = lista[i].split()
            del palavra[i]
			list.isert(palavra,i,lista[i].upper())
        i = i + 1
    return ' '.join(lista)