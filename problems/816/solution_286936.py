def maiores(a,n):
    a=tuple(a)
    for i in a:
        if n<i:
            lista.append(i)
    return tuple(list.sort(lista))