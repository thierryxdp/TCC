def fatorial (num):
    '''funcao que calcula e retorna o fatorial de um numero;
       int->int'''
    multiplicacao=1
    i=1
    while i<=num:
        multiplicacao=multiplicacao*i
        i=i+1
    return multiplicacao