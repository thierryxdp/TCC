# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que insere # no início, meio e fim"""
    h = len(s)//2
    k = len(s)/2
    p1=s[0:k]
    p2 = s[k+1:-1]
    p3 = s[0:h]
    p4 = s[h+1:-1]
    return '#' + p1 +'#' + p2 + '#'