# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que, dada uma string (com 0, 2 ou mais caracteres), retorna essa mesma string com uma hashtag no início, uma no meio e uma no final; str->str"""
    import math
    if(len(s)==0):
        return '###'
    else:
        a = len(s)
        s = s[0:(math.floor((a/2)))]+'#'+s[(math.floor((a/2))):-1]+s[-1]
        s = '#'+s
        s = s+'#'
        return s