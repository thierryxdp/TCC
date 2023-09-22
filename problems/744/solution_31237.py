# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    b = len(s)//2
    c = b + 1
    return "#" + s[0:b] + "#" + s[c:]