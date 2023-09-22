# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string com # no inicio, no meio e no final;
    str -> str"""
    if len(s)%2==0:
        return '#'+s[0:((len(s))/2)+1)]+'#'+s[((len(s))/2):]+'#'
    else:
        return '#'+s[0:(len(s)//2)+1]+'#'+s[(len(s)//2:]+'#'