# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao calcula e retorna '#' no inicio, meio e final de uma string""" 
    """str-->str"""
    import math
    m=math.floor(len(s)/2)
    return '#'+s[0:m:]+'#'+s[m:-1:]+'#'