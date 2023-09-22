def fatorial(numero):
    """ Função que dado um número, calcula o fatorial desse
        número;
        int -> int"""
    i = 1 #controla o número de iterações do while 
    fatorial = 1 #armazena a valor do fatorial no instante atual de i
    while i<numero:
        fatorial = fatorial *(i+1)
        i = i+1
    return fatorial