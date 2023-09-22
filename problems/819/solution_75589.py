def multiplos(lista,n):
    p=0
    multiplos=[]
    while p< len(lista):
        if lista[p]%n==0:
            multiplos=multiplos+(lista[p],)
        p=p+1
    return multiplos