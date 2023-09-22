def soma_h(num):
    ''''''
    soma = 0
    for n in range(num, 0, -1):
        soma += 1/n
    return round(soma, 2)