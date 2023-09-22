def fatorial(n):
    '''Função que recebe um número, calcula e retorna o fatorial desse número.
    Entrada: float. Saída: float'''
    contador=1
    acumulador=1
    while contador<=n:
        acumulador= acumulador*contador
        contador=contador+1
    return acumulador