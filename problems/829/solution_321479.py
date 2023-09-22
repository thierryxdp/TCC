def soma_h(n):
    '''Funcao que retorna o resultado de H  com 2 casas decimais.
    int->float'''
    x=range(1,n+1)
    soma=1
    for k in x:
        soma=soma+(1/k)
    return round(soma,2)