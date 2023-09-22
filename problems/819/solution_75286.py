def filtraMultiplos(lista,n):
    l=[]
    i=0
    while lista[i]%n==0:
        i=i+1
        list.insert(l,i,lista[i])
        return l