# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    r1 = s[:len(s)//2:]
    r2 = s[len(s)//2:]
    return str("#") + r1 + str("#") + r2 + str("#")