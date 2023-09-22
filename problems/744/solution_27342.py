# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    k = len(s)
    return s.join('#', ('',s[0:k/2], s[k/2:],' '))