def fatorial(num):
    '''Calcula o fatorial de um numero;
    int -> int'''
    
    resultado = 1

    while 0 < num:
        resultado *= num
        num -= 1
    
    return resultado