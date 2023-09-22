# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna uma string com hashtags inseridas no inicio, no meio e no fim 
    da string, dada a mensagem na entrada.
    str -> str'''
    import math
    
    metade = math.floor(len(s) / 2)
    
    return '#' + s[0:metade] + '#' + s[metade:] + '#'