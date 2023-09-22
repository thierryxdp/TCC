def maiores(lista,n):
    list.sort(lista)
    if lista[0]<n:
        i=0
        while lista[i]<n:
            del lista[i]
            i=i+1