def soma_h(N):
    '''função que calcula e retorna o valor de H co (N) termos
    onde (N) é inteiro, a função deve retornar o resultado
    somente com 2 casas decimais; int -> bool'''
    soma = 0
    for i in range(1,N+1):
        soma = soma + (1/(i*(i+1)))
    return soma