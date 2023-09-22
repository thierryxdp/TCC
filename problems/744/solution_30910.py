# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    y = x/2
    return "#" + s[0:y] + "#" + s[y+1:] + "#"