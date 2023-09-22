def soma_fatorial(num):
    '''Calcula e retorna o fatorial de um número
    int -> int''' 
    z = 1
    for i in range(1, num):
        z *= i
    return z