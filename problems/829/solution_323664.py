def soma_h(numero):
    '''função que calcula o valor de H fornecendo um numero natural como entrada
    int -> float'''
    soma = 0
    for k in range(1, numero + 1):
        soma = soma + 1/k
    return round(soma, 2)