def soma_h(n):
    '''retorna o resultado da soma 1 + 1/2 +...+1/n; int -> float'''
    samara = 1
    for i in range(n):
        if i == 0:
            samara += 0
        else:
            samara += 1/i
    return samara + 1/n