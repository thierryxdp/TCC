# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que adiciona "#" no inicio, meio e final da string.
    string -> string'''
    metade= len(s)//2
    return '#' + s[0:metade] + '#' + s[metade: len(s)] + '#'