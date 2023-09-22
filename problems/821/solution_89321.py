def fatorial(x):
    '''Função que dado um número x calcula e retorna o fatorial desse número: int -> int'''
    resultado = 1
    cnt = 1
    while cnt <= x:
        resultado *= cnt
        cnt += 1
    return resultado