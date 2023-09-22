def soma_h(n):
    '''função que dado como parametro um número inteiro n, calcula as divisões
    de 1 por n e retorna a soma de seus valores
    int->float'''
    soma=0
    for i in range(1,n+1):
        divisao=1/i
        soma=soma+divisao
    return round(soma,2)