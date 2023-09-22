from math import *
def primo(numero):
    '''
    Dado um número inteiro positivo retorna True se ele for primo
    e False se não for um número primo.

    Uso:
    primo(numero)

    Entrada:
    - número (int): Número inteiro positivo

     Saída:
    - Retorna se um dado número é primo ou não. (bool)
    '''
    qdt_div=0
    for n in range(1,numero+1):
        if numero%n==0:
            qdt_div=qdt_div+1
    if qdt_div==2:
        return True
    else:
        return False