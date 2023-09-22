from math import *

def quant_palavras(frase):
    '''Dada uma frase, conta a quantitade de palavras em uma frase

    Uso:
    quant_palavras(frase)

    Entrada:
    - frase (str, int, obrigatório): variavél 1

    Saída:
    - O numero de palavras da frase, considerando que a frase pode ter espaços no inicio e no final.
    '''
    return len(str.split(frase))