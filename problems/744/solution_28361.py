# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math

def hashtag(string):
    metade = math.floor(len(string)/2)
    concate = '#' + string[:metade] + '#' + string[metade:] + '#' 
    return concate