def fatorial(num):
    '''recebe um numero e calcula seu fatorial
    int->int'''
    
    teste = 1
    contador = 2
    while contador<=num:
        teste = teste*contador
        contador += 1
    return teste