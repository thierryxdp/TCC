def soma_h(n):
    '''função que calcula e retorna o valor H com N termos; int->int'''
    soma = 0
    for i in range(1,n+1):
        soma = soma + 1/i
    return round(soma,2)