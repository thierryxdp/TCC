def filtramultiplos(lista,n):
    lista=[]
    indece=0
    while lista[indece]>n:
        lista[indece]% n!=0
        list.append(lista,lista[indece])
        indece=indece+1
    return lista