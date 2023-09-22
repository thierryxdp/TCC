# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)
    s1 = l//2
    s2 = l - s1
    parte_1 = s[0:s2]
    return parte_1