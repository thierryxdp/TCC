def soma_h(n):
    '''Retorna o valor da função H de 1 a n;
int -> float'''
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    return soma