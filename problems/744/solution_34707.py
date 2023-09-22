# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''A função insere uma hashtag no ínício, meio e final
    de uma string. string -> string'''
    return '#'+s[:(len(s)//2)]+'#'+s[len(s)//2:]+'#'