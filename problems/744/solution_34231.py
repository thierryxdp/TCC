# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def parte(s):
    return len(s)//2

def hashtag(s):
    '''recebe uma string e insere o carcatere # no inicio, no meio e no fim dela'''
    return '#'+s[:parte(s)]+'#'+s[parte(s):]+'#'