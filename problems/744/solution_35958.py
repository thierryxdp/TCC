# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que retorna # no inicio, entre e no final """
    if len(s)//2:
     return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'
    elif len(s)//2+1:
     return '#'+s[0:len(s)//2+1]+'#'+s[len(s)//2+1:]+'#'