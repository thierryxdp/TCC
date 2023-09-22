def fatorial(n):
    '''Função que calcula o fatorial de um numero.int->int'''
    resultado=1
    i=1
    while i<=n:
        resultado=resultado*i
        i=i+1
    return resultado