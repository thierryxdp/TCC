# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    inicio = s[0:x//2]
    fim = s[(x//2):x]
    return str('#')+inicio+str('#')+fim+str('#')