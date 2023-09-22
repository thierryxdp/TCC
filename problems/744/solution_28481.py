# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Dado uma str, returna com o caracter '#' no inicio no meio e no fim.
    entrada: s -> str
    saida: str '''
    y='#'
    x=len (s)
    x=x//2
    return y + s [0:x] + y + s[x:] + y