def fatorial(numero):
    '''função que recebe um número e calcula o fatorial
    desse mesmo número.
    tipo de entrada: int
    tipo de saída: int'''
    
    i = 1
    numero_fat = 1

    while i <= numero:
        numero_fat = numero_fat * i
        i = i + 1
        
    return numero_fat