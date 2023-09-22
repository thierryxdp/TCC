def fatorial(n):
    ''' funcao retorna o fatorial de n. int->int'''
    i=n
    resultado=1
    while i>0:
        resultado*=i
        i-=1
    return resultado