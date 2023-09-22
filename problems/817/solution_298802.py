def acima_da_media(lista):
    a = []
    n=sum(lista)/len(lista)
    for elemento in lista:
        if elemento >= n:
            a.append(elemento)
            a.sort()
    return a
            b=sum(a)
            return b