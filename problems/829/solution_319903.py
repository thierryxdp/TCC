def soma_h(n):
    '''uma função que calcula a soma de 1 + 1/2... 1/n e retorna esse valor.
    int -> float'''
    soma = 0
    for i in range(n):
        soma +=1/i
    return round(soma, 2)