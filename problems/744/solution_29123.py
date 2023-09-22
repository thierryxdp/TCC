# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que insere o carectere "#" no início, meio e fim da string
    inserida"""
    n=len(s)
    return '#'+s[:(n//2)]+'#'+s[(n//2):]+'#'