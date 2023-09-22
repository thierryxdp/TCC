def uppCons (frase):
    lista = frase.split()
    i = 0
    while i<len(lista):
        if lista[i] in 'aeiou' : 
            lista = del lista[i] list.isert(lista,i,lista[i].upper())
        i = i + 1
    return lista