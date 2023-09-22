# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''str -> str
    coloca hashtags no inicio no meio e no final da str'''
    numletras=len(s)
    meio=numletras//2
    return '#'+s[:meio]+'#'+s[meio:]+'#'