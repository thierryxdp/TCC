# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """insere hastag na string s no começo, meio e fim dela
    str->str"""
    l=len(s)
    retorno='#'s[0,l/2]+'#'+s[l/2,l]+'#'
    return retorno