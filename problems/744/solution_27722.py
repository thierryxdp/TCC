# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return s[0:len('#')//2]+s+s[len('#')//2:len('#')]