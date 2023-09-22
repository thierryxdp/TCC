from math import *
def substitui(s,x,i):
    '''
    Dado uma string s, um caractere x e um número i entre 0 e o comprimento da string,
    retorna uma string igual a s, exceto que o elemento da posicao i deve ser substituido pelo caractere x.

    Uso:
    substitui(s,x,i)

    Entrada:
     - s (str, obrigatório): variavél 1
    - x (str, int, obrigatório): variavél 1
    - i (int, obrigatório): variavél 1

    Saída:
    - Uma string igual a s, onde o elemento da posicao i foi substituido pelo caractere x
    '''
    return s[0:i] + x + s[i + 1:]