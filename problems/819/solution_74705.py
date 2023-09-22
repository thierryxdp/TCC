def filtraMultiplos(lista,n):
    resposta=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            list.append(resposta,lista[proximo])
        proximo=proximo+1
    return resposta