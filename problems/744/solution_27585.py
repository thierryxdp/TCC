# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i=len(s)
    return '#' + s[0:i//2] + '#' + s[i//2:] + '#'