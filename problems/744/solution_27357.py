# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    m=int(len(s)/2)
    final='#'+s[0:m]+'#'+s[m:]+'#'
    return final