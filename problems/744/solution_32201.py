# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade= s//2
    return '#' + s[0:metade]+ '#' + s[metade:]+ '#'