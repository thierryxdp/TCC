# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=s[0:round(len (s))//2]
    y=s[round(len (s))//2:]
    return '''#'''+ x +'''#'''+ y +'''#'