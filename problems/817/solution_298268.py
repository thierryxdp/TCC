def acima_da_media(lista,n):

    a = []
    for elemento in lista:
        if elemento >= n:
            a.append(elemento)
            a.sort()