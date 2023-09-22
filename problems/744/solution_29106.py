# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    m = len(s)//2
    ret = '#' + s[:m] + '#' + s[m:] + '#'
    return ret