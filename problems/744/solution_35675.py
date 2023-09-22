# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a=len(s)//2
    b='#'+s[:a]+'#'+s[a:]+'#'
    return b