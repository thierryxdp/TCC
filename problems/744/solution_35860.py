# cria hashtags entre string
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    meio = math.floor(len (s) /2)
    return  '#' + s[:meio] + '#' + s[meio:] + '#'