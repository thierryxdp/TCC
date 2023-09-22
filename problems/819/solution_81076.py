def filtraMultiplos (lista, n):
    '''funcao que retorne lista com os divisiveis por n '''
    variavel=0
    listaA=[]
    
    while variavel<len(lista):
        if lista[variavel]%n==0:
            list.append(listaA,lista[variavel])
        variavel = variavel+1
        
    return listaA