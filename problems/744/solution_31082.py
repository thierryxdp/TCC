# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que, dada uma string (com 2 ou mais caracteres), retorna essa mesma string com uma hashtag no ínício, uma no meio e uma no final; str->str"""
    import math
    a = len(s)
    s = s[0:(math.floor((a/2)))]+'#'+s[(math.floor((a/2)):-1]+s[-1]
    s = '#'+s
    s = s+'#'