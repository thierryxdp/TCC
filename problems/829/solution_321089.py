def soma_h(n):
    '''função que retorna o valor h, com n termos onde n é inteiro
    int -> float'''
    soma = 0
    for x in range(1,n+1):
        soma += 1/x
    return soma