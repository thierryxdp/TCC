from math import *
def freq_palavras(frases):
    '''
    Dado uma string retorna um dicionário.

    Uso:
   freq_palavras(frases)

    Entrada:
    - frases (string): Chave de entrada

     Saída:
    - Retorna um dicionário em que cada palavra da mesma seja uma chave com o número de
    vezes que a palavra aparece. (dicionário)
    '''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario