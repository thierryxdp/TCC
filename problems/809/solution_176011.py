from math import *

def intercala(lista1, lista2):
    '''
    Dado as variaveis lista1 e lista2 de tamanho 3, gera-se uma nova variavel a lista3

    Uso:
    conta_frases(texto)

    Entrada:
    - lista 1 (lista, obrigatório): variavél 1
    - lista 2 (lista, obrigatório): variavél 2

    Saída:
    - Uma nova lista intercalando os elementos de lista1 e lista2. (lista)
    '''
    soma1 = lista1[0:1] + lista2[0:1]
    soma2 = lista1[1:2] + lista2[1:2]
    soma3 = lista1[2:] + lista2[2:]
    return soma1 + soma2 + soma3