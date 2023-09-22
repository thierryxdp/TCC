# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao que insere uma # no inicio, meio e fim de uma string"""
    """str -> str"""
    metade = len(s) // 2
    return '#'+s[:metade]+'#'+s[metade:]+'#'