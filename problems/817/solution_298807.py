def acima_da_media(lista):
    a = []
    n=sum(lista)/len(lista)
    if len(lista) == 1:
        return []
    elif 0 in lista:
        n = sum(lista) / len(lista)-1
        for elemento in lista:
            if elemento >= n:
                a.append(elemento)
                a.sort()
        return a
    else:
    for elemento in lista:
        if elemento >= n:
            a.append(elemento)
            a.sort()
    return a