def soma_h(n):
    '''dado um número inteiro n, retorna o valor h seguindo a
    fórmula: h = (1 + 1/2 + 1/3 + ... + 1/n) com n termos;
    int --> float'''
    soma = 0
    for num in range(1,n+1):
        soma = soma + 1/num
    return round(soma,2)