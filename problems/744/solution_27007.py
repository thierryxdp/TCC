# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ """
    metade = len (s) /2
    tam = len (s)
    retorno = '#'+ s[0:metade] + '#' + s[metade:] + '#' 
    return retorno