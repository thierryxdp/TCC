def faltante(numeros):
    '''retorna o numero faltante do intervol [1,N]
    list->int'''
    N=numeros[-1]
    pa=N*(N+1)/2
    soma=sum(numeros)
    
    if pa=sum(numeros):
        return [numeros,numeros[-1]+1]
    return pa-sum(numeros)