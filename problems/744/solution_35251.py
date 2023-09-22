# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere uma hashtag # no meio da string inserida'''
    tamanho = len(s)
    hashtag = '#'+s[:tamanho/2]+'#'+s[tamanho/2:]+'#'
    return hashtag