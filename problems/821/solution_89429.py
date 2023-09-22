def fatorial(numero):
    '''dado um numero(numero), retorna o fatorial do mesmo; int -> int'''
    multiplo = numero
    multi = 1
    if numero == 0:
        return 1 
    else:
        while numero > 0:
            multi = multi * numero 
            numero = numero - 1
        return multi