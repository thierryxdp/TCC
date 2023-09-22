#Exercício_04: 
''' Essa função substitui a pontuação de uma frase por " " (espaços). '''
''' str ---> str. '''

import re

def punctuation_elimination(string_text):
    return re.sub(r"[-,:;.?!]", " ", string_text)