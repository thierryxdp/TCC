def filtraMultiplos(lista,n):
    proximo=0
    Multi=[]
    while proximo<len(lista):
        m=lista[proximo]%n
        if m==0:
            list.append(Multi,lista[proximo])
        proximo=proximo+1
    return Multi