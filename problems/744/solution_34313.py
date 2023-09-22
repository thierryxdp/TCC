# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pre = s[ :len(s)//2]
    pos = s[len(s)//2: ]
    return "#" + pre + "#" + pos + "#"