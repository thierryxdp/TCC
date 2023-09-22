# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)
    return str('#')+s[0:x//2]+str('#')+s[x//2:]+str('#')