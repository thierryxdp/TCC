# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s = '#' + s[0:2:1] + '#' + s[2:] + '#'
    return s