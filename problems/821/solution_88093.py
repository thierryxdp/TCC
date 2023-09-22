def fatorial(num):
    '''retorna o fatorial de um número dado;
    int->int'''
    resultado=1
    i=1
    while i<=num:
        resultado=resultado*i
        i=i+1
    return resultado