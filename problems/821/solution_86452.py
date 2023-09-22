def fatorial(valor):
    ''' Retorna o fatorial do valor indicado.
        int -> int'''
    fatorial = 1  
    while (valor > 1):
        fatorial = fatorial * valor  
        valor = valor - 1  
    return fatorial