"""Retorna uma string com o caractere '#' no
inicio,no meio e no fim da string dada."""  
import math
def hashtag(s):
    nome = s
    return '#' + nome[0:math.floor(len(nome)/2)] + '#' + nome[math.floor(len(nome)/2):] + '#'