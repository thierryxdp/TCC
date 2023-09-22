# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna uma string com # no início, no meio e no final.
    str-> str'''
    a=int(len(s)/2)
    return '#'+s[:a]+'#'+s[a:]+'#'