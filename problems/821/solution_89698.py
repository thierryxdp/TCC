def fatorial(y):
    '''funcao que retorna o fatorial de um numero y
    int->int'''
    x=1
    while y!=1:
        x=y*x
        y=y-1     
    return x