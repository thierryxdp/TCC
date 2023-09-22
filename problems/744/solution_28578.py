# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e insere # no início,
    meio e fim dela;
    str->str"""
    x=len(s)
    y=len(s)//2
    return '#'+s[0:y]+'#'+s[y,x]+'#'