def soma_h(n):
    '''função que retorna o valor de h com n termos inteiros'''
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)