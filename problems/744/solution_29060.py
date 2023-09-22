# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insire '#' no inicio no meio e no final da string;
    str-> str'''
    x=len(s)//2
    return '#'+s[:x]+'#'+s[x:]+'#'