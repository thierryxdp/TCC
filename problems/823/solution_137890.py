def faltante(numeros):
    '''retorna o numero faltante do intervol [1,N]
    list->int'''
    N=numeros[-1]
    pa=N*(N+1)/2
    soma=sum(numeros)

    return pa-sum(numeros)