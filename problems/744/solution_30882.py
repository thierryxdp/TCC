# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função retorna hashtag no inicio, meio e fim da string"""
    t = len(s)
    y = t//2
    return '#'+s[0:y]+'#'+s[y:]+'#'