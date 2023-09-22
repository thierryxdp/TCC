# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    y=len(s)
    return "#" + s[0:y//2] + "#" + s[y//2:90] + "#"