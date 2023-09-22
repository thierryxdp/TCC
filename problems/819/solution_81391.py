def filtraMultiplos(lista,n):
    variavel=0
    listaA=[]
    
    while variavel<len(lista):
        if lista[variavel]%n==0:
            list.append(listaA,lista[variavel])
        variavel = variavel +1
    return listaA