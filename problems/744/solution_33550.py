# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que insere uma # no incio, meio e fim da string"""
    m=(len(s))//2
    a=s[0:m]
    b=s[m:]
    return '#'+a+'#'+b+'#'