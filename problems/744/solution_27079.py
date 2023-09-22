# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    d = len(s)/2
    return s[:int(d)] + s + s[int(d):]