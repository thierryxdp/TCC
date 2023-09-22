# a funçao primeiro coloca uma # no começo depois quebra ela em duas partes
# adicionadno uma # no meio e a +  a outra parte e uma # no final
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    parte_1 = s[0:math.floor(len(s)/2)]
    parte_2 = s[math.floor(len(s)/2):len(s)]
    return '#' + parte_1 + '#' + parte_2 + '#'