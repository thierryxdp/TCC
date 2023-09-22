def maiores(numeros, n):
    a= numeros
    list.extend(numeros,[n])
    a.sort()
    b= list.index(a, n)
    return a[b+1:]