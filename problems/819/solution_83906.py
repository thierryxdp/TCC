from random import randint
def jogo_2dados():
    '''Função que simula um jogo de dois dados com valores arbitrários
    ao contar quantas vezes foram jogados até sair números repetidos.
    sem entrada => int'''
    simula_contar= 0
    dado1 =1
    dado2 =2
    while dado1 != dado2:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        simula_contar += 1
    return simula_contar