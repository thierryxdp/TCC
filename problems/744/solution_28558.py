# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s2 = len(s)
    s3 = int(s2/2)
    s4 = '#' + s[0:s3] + '#' + s[s3:] + '#'
    return s4