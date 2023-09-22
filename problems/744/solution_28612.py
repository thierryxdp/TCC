# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i=len(s)
    s='#'+s[:i//2]+'#'+s[i//2:i]+'x'
    return s