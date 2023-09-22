def filtraMultiplos(lista,num):
    l=[]
    i=[]
    while i<len(lista):
        if lista[i]%num==0:
            l.insert(i,lista[i])
        i+=1
    return l