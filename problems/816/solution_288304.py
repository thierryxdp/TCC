def maiores(list_n,n):
    x = 0
    soma = 0
    while x<len(list_n):
        if list_n[x]>n:
            lista=list_n[x]
        x+=1
    lista=list_n.sort()
    return lista