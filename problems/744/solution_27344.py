# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    k = len(s)
    j = round(k-0.5)
    m = round(k+0.5)
    return s.join('#', ('',s[0:j], s[m:],' '))