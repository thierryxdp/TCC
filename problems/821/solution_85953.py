def fatorial(numero):
    '''fatorial recebe um numero inteiro e devolve o fatorial desse numero
    determina de um numero 
    int --> int'''
    contador = numero
    fatorial = 1
    while contador>0:
        fatorial = fatorial*contador
        contador -=1
    return fatorial