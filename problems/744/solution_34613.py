# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Insere o caracter # no inicio, meio e fim da string'''
    string = '#'+s[0:len(s)/2]+'#'+s[len(s)/2:]+'#'
    return string