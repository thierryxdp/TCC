from math import *

def conta_frases(texto):
    '''
    Dado um texto conta a quantidade de frases

    Uso:
    conta_frases(texto)

    Entrada:
    - texto (str, obrigatório): variavél 1

    Saída:
    - A quantidade de frases que o texto possui.'''

    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')