def soma_h(n):
    '''dado n, inteiro, retorna o valor da expressao
    int -> float'''
    soma = 0
    for i in range(1, n+1):
        soma += 1/i
    round(soma, 2)
    return soma