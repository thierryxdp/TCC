# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Para por uma #no inicio, meio e fim a sua string, digite;
    str->str"""
    if len(s)==2:
        return '#'+s[0:1]*2+'#'+s[1:2]*2+'#'