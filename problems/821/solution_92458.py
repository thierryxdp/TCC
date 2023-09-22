def fatorial(n):
    '''Função que retorna o fatorial de um numero n
    entrada - int
    saida - int'''
    i=1
    resultado=1
    while i<=n:
        resultado+resultado*i
        i=i+1
    return resultado