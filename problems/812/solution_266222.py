def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    
from functools import reduce
frase = reduce(lambda t, s: t.replace(s, ''), simbolos_pontuacao, frase)