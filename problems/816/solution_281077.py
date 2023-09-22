def maiores(lista,n):
    novalista=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]>n:
            novalista=novalista+[lista[proximo]]
        proximo=proximo+1
    return list.sort(novalista)