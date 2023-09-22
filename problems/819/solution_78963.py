def filtraMultiplos(lista,n):
    novalista=[]
    proximo=0
    while proximo<=len(lista)-1:
        if lista[proximo]%n==0:
            novalista=novalista+[lista[proximo]]
        proximo=proximo+1
    return novalista