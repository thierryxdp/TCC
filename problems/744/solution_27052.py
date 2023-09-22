# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """dado uma string coloca # no ínicio,meio e fim dela"""
    if len(s) != 0 and len(s) != 1:
        new = list(s)
        new[0] = '#' + s[0]
        new[len(s)//2] = '#' + s[len(s)//2]
        new[-1] = s[-1] + '#' 
        return ''.join(new)
    elif len(s) != 1:
        return '###'
    else:
        return '##'+s+'#'