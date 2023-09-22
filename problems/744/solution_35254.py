# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere uma hashtag # no meio da string inserida'''
    a = len(s)/2
    hashtag = '#'+s[0:a]+'#'+s[a:]+'#'
    return hashtag