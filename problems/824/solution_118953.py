def uppCons(frase):
    i = 0
    lista1 = list(frase)
    while i in range(len(frase)):
        if frase[i] in ('a','e','i','o','u','á','à','é','ó','ô','â'):
            lista1.remove(frase[i])
        i = i + 1
    return str.upper(str.join('',lista1))