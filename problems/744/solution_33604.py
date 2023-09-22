# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere uma # no inicio, meio e final de uma string'''
    j = s[0:math.floor(len(s)/2)]
    k = s[math.floor(len(s)/2):len(s)]
    
    return '#' + j + '#' + k + '#'