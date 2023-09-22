def maiores(a,n):
    lista=[]
    for i in a:
        if n<i:
            lista.append(i)
    return list.sort(lista)