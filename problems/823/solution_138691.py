def faltante(l=[1,2]):
    lista=[]
    l[-1]=0
    f=0
    i=0
    for x in l:
        y=int(l[i-1])
        if x-y!=1:
            lista.append(x-1)
        i=i+1
    return lista