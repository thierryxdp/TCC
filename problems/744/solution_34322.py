# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    y=len(s)//2
    a=(s[ :y])
    b=(s[y: ])
    return'#'+str(a)+'#'+str(b)+'#'