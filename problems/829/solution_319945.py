def soma_h(N):
    '''Função que retorna a soma de H dado um inteiro N.
    int->float'''
    soma=0
    for c in range(1,N+1):
        sobre=(1/c)
        soma=soma+sobre
    return round(soma,2)