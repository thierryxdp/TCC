# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna s com '#'inserido no início, meio e final dela.
    str->str"""
    return '#'+str(s[0:(len(s)//2)])+'#'+str(s[((len(s)//2)+1):-1])+'#'