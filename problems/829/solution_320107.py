def soma_h(n):
    '''função que calcula e retorna o valor H com N termos; int->int'''
    soma = 0
    for i in range(1,n+1):
        soma = round(soma)+(i)/(n-1)
    return round(soma,2)