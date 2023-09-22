def faltante(numeros):
    '''retorna o numero faltante do intervalo [1,N]
    list->int'''
    N=numeros[-1]
    pa=N*(N+1)/2
    soma=sum(numeros)
    if pa>soma:
        return pa-soma
    if pa==soma:
        numero=numeros[-1]+1
        return numero
          
 #não consegui pensar em uma solução utilizando o while