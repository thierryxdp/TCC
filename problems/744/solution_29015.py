# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que insere # no início, meio e fim"""
    h = int(len(s)//2)
    k = int(len(s)/2)
    p1 = s[0:k]
    p2 = s[k:]
    p3 = s[0:h]
    p4 = s[h:]
    if k//2 == k/2:
        return '#' + p1 + '#' + p2 + '#'
    else:
        return '#' + p3 +'#' + p4 + '#'