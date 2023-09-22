def faltante(numeros):
    '''retorna o numero faltante do intervol [1,N]
    list->int'''
    N=numeros[-1]
    pa=N*(N+1)/2
    soma=sum(numeros)
    if pa>soma:
        return pa-soma
    if pa==soma:
        nova_lista=numeros.append(numeros[-1]+1)
        return nova_lista