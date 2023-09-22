def maiores(a,n):
    list.sort(a)
    lista=[]
    for i in a:
        if i>n:
            lista.append(i)
    return lista