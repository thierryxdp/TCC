def soma_h(N):
    ''' função que recebe um numero inteiro N como entrada e retorna o valor
H=1+1/2+1/3+1/4+...+1/N, ou seja, o somatório de 1/k, com k indo de 1 até N;
int->float'''

    soma=0
    for x in range(1,N+1):
        soma=soma+(1/x)
    return round(soma,2)