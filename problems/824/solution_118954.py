def uppCons(frase):
    i = 0
    lista1 = list(frase)
    while i in range(len(frase)):
        if not frase[i] in ('a','e','i','o','u','á','à','é','ó','ô','â'):
            del lista1[i]
            list.insert(lista1,i,str.upper(frase[i]))
        i = i + 1
    return str.join('',lista1)