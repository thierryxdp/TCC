def filtrarMultiplos(lista,n):
    prox= len(lista)
    resp=[]
    i=0
    while prox>i:
        if lista[i]%n==0:
            resp=[lista[i],]
        i=i+1
        return resp