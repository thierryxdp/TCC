# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna # no início meio e fim da sua string (s)
    str -> str'''
    return '#'+[:len(s)//2]+'#'+[len(s)//2:]+'#'