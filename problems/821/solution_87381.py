#---------------------EXERCICIO 5---------------------

def fatorial(numero):
    '''Retorna o fatorial de um numero
       int-> int'''

    i = numero-1                #contador
    fatorialNumero = numero     #acumulador
    
    while i>1:
        fatorialNumero *= i
        i-=1

    return fatorialNumero