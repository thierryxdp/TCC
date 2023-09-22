# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funçao que insere # no comeco, meio e final da string.
    string - > string"""
    x = (len(s)//2)
    return '#'+s[0:x]+'#'+s[x:]+'#'