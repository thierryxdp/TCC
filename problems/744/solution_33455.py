# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dado uma string s, retorna a string com # no inicio, meio e fim da mesma'''
    return '#'+s[:(int(len(s)/2))]+'#'+s[(int(len(s)/2)):]+'#'