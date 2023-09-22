def filtraMultiplos(l,n):
    lista=[]
    i=0
    while i <= range(len(l)):
        if (l[i]//n)%2==0:
            lista= lista+ (l[i], )
        i=i+1
        return lista