# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funçao que dada uma string retorna ela com # no inicio meio e fim'''
    metade = int(len(s)/2)
    return '#'+s[:metade]+'#'+s[metade:]+'#'