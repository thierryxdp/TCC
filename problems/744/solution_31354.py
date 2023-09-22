# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashyag(s):
    """coloca # no inicio,meio e fim de uma string
    string->string"""
    meio = math.floor(len(s)/2)
    return '#' + s[:meio] + '#' + s[meio:] + '#'