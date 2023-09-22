def fatorial(numero):
    '''
Função que dado um número, calcula e retorna o fatorial
desse número.

int-->int
    '''
    fat=1
    while numero>=1:
        fat=fat*numero
        numero=numero-1
    return fat