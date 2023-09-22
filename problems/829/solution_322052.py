def soma_h(N):
    '''Recebe um número natural N e retorna a soma 1 + 1/2 + 1/3 + 1/4 + ... + 1/N; int -> float'''
    soma = []
    for i in range (1, N+1):
        soma += [(1/i)]
    return round(sum(soma),2)