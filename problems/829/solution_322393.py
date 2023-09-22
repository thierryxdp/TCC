def soma_h(n):
    '''retorna a soma dos inversos de n numeros
    int->float'''
    lista=list(range(1,n+1))
    soma=0
    for elemento in lista:
        soma=soma+(1/n)
    return round(soma,2)