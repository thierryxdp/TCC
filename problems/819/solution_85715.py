def filtraMultiplos(l,n):
    i=0
    lista=[]
    while range(len(l)):
        if (l[i]//n)%2 ==0:
           lista = list.append(lista,l[i])
    return lista