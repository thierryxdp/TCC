def soma_h(numero):
    '''funcao que retorna um resultado com 2 casas decimais
    int->float'''
    soma=0
    f=range(1,numero+1)
    for c in f:
        soma=soma+(1/c)
    return round(soma,2)